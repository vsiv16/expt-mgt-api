import itertools

def parameter_combinations_orig(func):
    def wrapper(*args, **kwargs):
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    kwargs['param1'] = i
                    kwargs['param2'] = j
                    kwargs['param3'] = k
                    func(*args, **kwargs)
    return wrapper


def parameter_combinations(param1_range, param2_range, param3_range):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in param1_range:
                for j in param2_range:
                    for k in param3_range:
                        kwargs['param1'] = i
                        kwargs['param2'] = j
                        kwargs['param3'] = k
                        func(*args, **kwargs)
        return wrapper
    return decorator


def parameter_lists(param1_list, param2_list, param3_list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in param1_list:
                for j in param2_list:
                    for k in param3_list:
                        kwargs['param1'] = i
                        kwargs['param2'] = j
                        kwargs['param3'] = k
                        func(*args, **kwargs)
        return wrapper
    return decorator

def parameter_combinations_generalized(*params):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for values in itertools.product(*params):
                print("VALUES: ", values)
                for i, value in enumerate(values):
                    kwargs[f"param{i+1}"] = value
                func(*args, **kwargs)
        return wrapper
    return decorator


def param_combos_gen_names(**params):
    # IN PROGRESS
    def decorator(func):
        def wrapper(*args, **kwargs): # args, kwargs empty initially

            print("PARAMS: ", params) # dictionary (param name: param value)
            print("*PARAMS: ", *params) # only key names
            print("PARAMS KEYS: ", list(params.keys()))
            param_names = list(params.keys())

            # prep list of value lists for itertools product
            # ex for params: {'p1': [1, 2, 3], 'p2': [1, 2], 'p3': [1, 2, 3, 4]}
            # vals_list is [[1, 2, 3], [1, 2], [1, 2, 3, 4]]
            vals_list = []
            for key in params:
                vals_list.append(params[key])
            print("VALS_LIST: ", vals_list)

            # iterate through all possible parameter value combinations
            for values in itertools.product(*vals_list):
                # print("VALUES PRODUCT: ", values)

                for i, value in enumerate(values):
                    param_name = param_names[i]
                    # print(i, param_name, value)
                    kwargs[param_name] = value

                # call func for every combination of param values
                func(*args, **kwargs)

        return wrapper
    return decorator


def param_no_combos_gen_names(**params):
    def decorator(func):
        def wrapper(*args, **kwargs): # args, kwargs empty initially
            print("PARAMS: ", params) # dictionary (param name: param value)
            print("*PARAMS: ", *params)
            for param_name in params:
                print("KEY: ", param_name)
                value = params[param_name]
                print("VALUE: ", value)
                kwargs[param_name] = value
            func(*args, **kwargs)
        return wrapper
    return decorator
