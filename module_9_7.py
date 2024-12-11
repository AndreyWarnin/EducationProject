def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, *kwargs)
        wrapper_result = 'Простое'
        for divisor in range(2, result):
            if result % divisor == 0:
                wrapper_result = 'Составное'
                break
        return wrapper_result
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

print(sum_three(2, 3, 6))