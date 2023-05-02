import pandas as pd
import itertools

def experiment_entry(*args, **kwargs):
    def inner_decorator(func):
        def wrapper(*args, **kwargs):

            # TODO: create new output folder -- named "Run_timestamp"
            # TODO: save a copy of user's code in output folder -- named "Version_timestamp??"

            param_names = list(kwargs.keys())
            param_options = list(kwargs.values())

            column_names = param_names + ["Model Output"]
            df = pd.DataFrame(columns=column_names)
            for index in range(len(param_options[0])):
                save_info = []
                for p in param_options: 
                    save_info.append(p[index])
                save_info.append(func(save_info)) # CALL MODEL
                df.loc[len(df.index)] = save_info
            df.index = ["Experiment " + str(i+1) + ":" for i in range(len(df.index))]
            styled_df = df.style.format({'Model Output': lambda x: f'<span style="background-color: yellow">{x}</span>'})
            # print(styled_df)

            # TODO: download csv & save into output folder

            return styled_df

        return wrapper
    return inner_decorator

# p1 = [1, 2, 3]
# p2 = [4, 5, 6]
# # every_combination = False

# @experiment_entry(p1=p1, p2=p2)
# def model(p1=p1, p2=p2):
#     print("Inside the function.")

# model(p1=p1, p2=p2)