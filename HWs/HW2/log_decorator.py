import functools
from datetime import datetime

def function_logger(fileName: str):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with open(fileName, 'a+') as log:
                t1 = datetime.now()
                res = func(*args, **kwargs)
                t2 = datetime.now()
                
                log.write("\n--------------------------------\n")
                log.write(f"Название функции: {func.__name__}\n")
                log.write(f"Время вызова функции: {t1}\n")
                log.write(f"Входящие аргументы: {tuple(args), dict(**kwargs)}\n")
                log.write(f"Возвращаемое значение: {res if res else "-"}\n")
                log.write(f"Время завершения работы функции: {t2}\n")
                log.write(f"Время работы функции: {t2 - t1}c\n")
                log.write("--------------------------------\n")
        return wrapper
    return decorator


# @function_logger('test.log')
# def greeting_format(name, qwe, qwee):
#     [i for i in range(10000000)]
#     return f'Hello, {name}!'

# greeting_format(name="asdasd", qwe="fghjgfhj", qwee="John")