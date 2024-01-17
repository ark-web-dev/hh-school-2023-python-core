import time

def start_end_log_decorator(target_function):
    def inner_func(*args, **kwargs):
        start_time = time.time()

        print(' -------- LOG INFO --------')
        print(f'Метод: {target_function.__name__}')
        print(f'Start Time: {start_time}')

        target_function_result = target_function(*args, **kwargs)
        end_time = time.time()

        print(f'End Time: {end_time - start_time}. Время выполнения: {end_time - start_time}')
        print(' -------- LOG INFO --------\n')

        return target_function_result
    return inner_func
