from functools import wraps


def type_logger(level=0):

    def logger(func):

        @wraps(func)
        def decor(*args, **kwargs):
            total_args=list(args)+list(kwargs.values())
            res=func(total_args[0])
            if level==1:
                print(','.join([f'{x}:{type(x)}' for x in total_args]))
            elif level==2:
                print(f'{func.__name__}:{type(func)}')
                print(f'{func.__name__}({total_args[0]}):{type(res)}')
            return res

        return decor

    return logger


@type_logger(2)
def calc_cube(x):
    return x ** 3

if __name__=='__main__':
    a=calc_cube(5,6, val=4)
    print(a)
