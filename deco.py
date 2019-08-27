def uppercase_decorator(function):
    def wrapper():
        print('we are')
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


@uppercase_decorator
def say_hi():
    print('dercoirted')
    return 'hello there'


# decorate = uppercase_decorator(say_hi)
# print(decorate())
say_hi()
