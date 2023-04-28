import pandas as pd
import itertools

class ExperimentManager:
    def __init__(self, model, params, param_names, every_combination=False):
        self.model = model # function type?
        self.param_names = param_names # ??
        self.params = params
        self.every_combination = every_combination
        
    def run_experiment(self):
        '''Runs experiment. <todo: update this docstring>'''
        # self.model(self.params)

        if self.every_combination:
            print(list(itertools.product(*self.params)))
        column_names = self.param_names + ["Model Output"]
        df = pd.DataFrame(columns=column_names)
        for index in range(len(self.params[0])): 
            save_info = []
            for p in self.params: 
                save_info.append(p[index])
            save_info.append(self.model(save_info))
            df.loc[len(df.index)] = save_info
        df.index = ["Experiment " + str(i+1) + ":" for i in range(len(df.index))]
        styled_df = df.style.format({'Model Output': lambda x: f'<span style="background-color: yellow">{x}</span>'})
        return styled_df