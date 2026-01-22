def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function")
        start_time = time.time()
        res = func(*args, **kwargs)

        print("After function")
        end_time = time.time()
        print(f"Time taken: {end_time - start_time} seconds")
        return res
    return wrapper


def show_arguments(*args, **kwargs):
    print(f"args (tuple): {args}")
    print(f"kwargs (dict): {kwargs}")

    # * and ** are used to unpack the arguments and kwargs
    # * is used to unpack the tuple
    # ** is used to unpack the dictionary
    args_list = [1, 2, 3]
    kwargs_dict = {"name": "Alice", "age": 25}
    print(f"args (tuple): {[*args_list]}")
    print(f"kwargs (dict): {{**kwargs_dict}}")

    args_list = [1, 2]
    kwargs_dict = {"name": "Alice", "age": 25}
    print(f"args (tuple): {args_list}")
    print(f"kwargs (dict): {kwargs_dict}")
    
    

if __name__ == "__main__":  
    show_arguments(1, 2, 3)
    show_arguments(1, 2, name="Alice", age=25)
    show_arguments(x=10, y=20)