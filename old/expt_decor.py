
# def experiment_entry(func):
#     def wrapper_do_experiment(*args, **kwargs):
#         # code before for processing parameters
#         print("hi", args[0], kwargs)
#         func(**kwargs)
#         func(**kwargs)
#         # code after for saving outputs
#     return wrapper_do_experiment

# definition
# def my_decorator(param1, param2):
#     def inner_decorator(func):
#         def wrapper(*args, **kwargs):
#             print("Before the function is called.")
#             result = func(*args, **kwargs)
#             print("After the function is called.")
#             return result
#         return wrapper
#     return inner_decorator

def my_decorator(*args, **kwargs):
    def inner_decorator(func):
        def wrapper(*args, **kwargs):
            print("Before the function is called.")
            result = func(*args, **kwargs)
            print("After the function is called.")
            return result
        return wrapper
    return inner_decorator






