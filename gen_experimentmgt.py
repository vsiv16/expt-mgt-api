import itertools
import pandas as pd
import os
from datetime import datetime
import pickle

def experiment_entry(**params):
    def decorator(func):
        def wrapper(*args, **kwargs): # args, kwargs empty initially

            # TODO: create new output folder -- named "Run_timestamp"
            # Get the current working directory path
            cwd = os.getcwd()
            log_records_path = os.path.expanduser(cwd + "/.log_records")

            # Create the directory if it doesn't exist already
            if not os.path.exists(log_records_path):
                os.makedirs(log_records_path)

            # Current timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
            current_saving_folder = os.path.expanduser(cwd + "/.log_records/run_" + timestamp)
            if not os.path.exists(current_saving_folder):
                os.makedirs(current_saving_folder)

            # TODO: save a copy of user's code in output folder -- named "Version_timestamp??"
            # Go through all files in the current working directory
            serialise_all_files(cwd, current_saving_folder)
            
            # Serialise them and save in current_saving_folder

    

            #######################################################################
            # print("PARAMS: ", params) # dictionary (param name: param value)
            # print("*PARAMS: ", *params) # only key names
            # print("PARAMS KEYS: ", list(params.keys()))
            param_names = list(params.keys())

            # prep list of value lists for itertools product
            # ex for params: {'p1': [1, 2, 3], 'p2': [1, 2], 'p3': [1, 2, 3, 4]}
            # vals_list is [[1, 2, 3], [1, 2], [1, 2, 3, 4]]
            vals_list = []
            for key in params:
                vals_list.append(params[key])
            # print("VALS_LIST: ", vals_list)

            # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
            column_names = param_names + ["Model Output"]
            df = pd.DataFrame(columns=column_names)
            # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #

            # run all experiments: iterate through all possible parameter value combinations
            for values in itertools.product(*vals_list):
                expt_info = []
                # print("VALUES PRODUCT: ", values)
                
                # prep params for each experiment 
                for i, value in enumerate(values):
                    param_name = param_names[i]
                    kwargs[param_name] = value
                    # $$$$$$$$$$$$$$$$$$$$$ #
                    expt_info.append(value)
                    # $$$$$$$$$$$$$$$$$$$$$ #

                # run experiment (call func for each combination of param values)
                output = func(*args, **kwargs)
                # print(output)
                # $$$$$$$$$$$$$$$$$$$$$ #
                expt_info.append(output)
                # $$$$$$$$$$$$$$$$$$$$$ #
                df.loc[len(df.index)] = expt_info
            #######################################################################

            # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
            df.index = ["Experiment " + str(i+1) + ":" for i in range(len(df.index))]
            styled_df = df.style.format({'Model Output': lambda x: f'<span style="background-color: yellow">{x}</span>'})
            # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #

            # TODO: download csv & save into output folder
            save_output(df, current_saving_folder, func)

            return styled_df

        return wrapper
    return decorator


def serialise_all_files(cwd, current_saving_folder):
    for filename in os.listdir(cwd):
        # print(filename)
        if filename[0] == '.':
            continue
        f = os.path.join(cwd, filename)
        # checking if it is a file
        if os.path.isfile(f):
            serialise(filename, cwd, current_saving_folder)
        else:
            # print("recursion")
            serialise_all_files(f, current_saving_folder)


def serialise(filename, cwd, current_saving_folder):
    # print("File to be serialised ", filename)
    # open the file for reading
    with open(os.path.join(cwd, filename), 'rb') as file:
        # read the contents of the file
        file_contents = file.read()

    # serialize the data using pickle
    serialized_file = pickle.dumps(file_contents)

    # open a new file for writing
    dir_to_be_saved_in = current_saving_folder + cwd
    if not os.path.exists(dir_to_be_saved_in):
        os.makedirs(dir_to_be_saved_in)
    with open(dir_to_be_saved_in+"/"+filename+'.pickle', 'wb') as new_file:
        # write the serialized data to the new file
        new_file.write(serialized_file)

def save_output(df, current_saving_folder, func):
   # Find the index of the first space character
    func_string = str(func)
    first_space = func_string.find(" ")
    second_space = func_string.find(" ", first_space + 1)

    # Extract the substring between the first and second space characters
    func_name = func_string[first_space+1:second_space]

    output_file_path = os.path.expanduser(current_saving_folder + "/" + func_name + "_out.csv")
    df.to_csv(output_file_path) 




