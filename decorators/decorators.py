def new_decorator(orig_func):
    def wrap_func():
        print("before the func ")
        orig_func()
        print("after the func")

    return wrap_func


@new_decorator
def func_to_be_decorated():
    print('func_to_be_decorated')


func_to_be_decorated()
