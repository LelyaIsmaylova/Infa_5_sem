import datetime

def log_func_call(log_file):
    def decorator(func):
        def wrapper(*args, **kwargs):
            starting_time = datetime.datetime.now()
            result = func(*args, **kwargs)
            ending_time = datetime.datetime.now()
            execution_time = ending_time - starting_time
            with open(log_file, "a") as file:
                file.write(f"Время вызова функции: {starting_time}\n")
                file.write(f"Входящие аргументы: args={args}, kwargs={kwargs}\n")
                file.write(f"Ответ return: {result if result is not None else '-'}\n")
                file.write(f"Время завершения работы функции: {ending_time}\n")
                file.write(f"Время работы функции: {execution_time}\n\n")
            return result
        return wrapper
    return decorator

@log_func_call("log.log")
def example(a, b):
    return a + b

example(1, 2)
