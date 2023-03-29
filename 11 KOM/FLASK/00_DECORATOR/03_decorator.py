def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print('display function ran well')

@decorator_function
def display_info(name, age, school):
    print('display info ran with argument ({} {} {})'.format(name, age, school))

#decorator_function(display)
display()
display_info("Thomas", 18, school="IGS")