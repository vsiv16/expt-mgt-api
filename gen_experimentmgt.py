import itertools
import pandas as pd

def experiment_entry(**params):
    def decorator(func):
        def wrapper(*args, **kwargs): # args, kwargs empty initially

            # TODO: create new output folder -- named "Run_timestamp"
            # TODO: save a copy of user's code in output folder -- named "Version_timestamp??"

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

            return styled_df

        return wrapper
    return decorator