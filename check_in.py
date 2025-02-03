def check_in(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + 10 if isinstance(result, int) else result
    return wrapper

@check_in
def get_number(x):
    return x * 2  # можна і інші

# результат
print(get_number(5))  # виведе 20 (10 + 10)
print(get_number(3.5))  # виведе 7.0 без змін
