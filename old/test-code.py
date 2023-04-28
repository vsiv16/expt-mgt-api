import pandas as pd
# import itertools
import exptmgt as exptmgt

# parameters to try out for model and to track the outputs for 
p1 = [1, 2, 3] # different values you want to try for p1
p2 = [4, 5, 6] # diffrent values you want to try for p2 
every_combination = False # if set to true will try out every combination of p1 with p2

params = [p1, p2]
param_names = ["p1", "p2"]

def model(params):
    temp_output = 0 
    for p in params:
        temp_output += p
    return temp_output

# ************ #
expt_mgr = exptmgt.ExperimentManager(model, params, param_names, every_combination)
expt_mgr.run_experiment()