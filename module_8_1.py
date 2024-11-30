def add_everything_up(a, b):
    try:
        result = a + b
        return result
    except TypeError as te:
        return f'{a}{b}'

print(add_everything_up(1, 5))
print(add_everything_up(2.56, 5))
print(add_everything_up(5, 5.219))
print(add_everything_up(3.968, 5.219))

print(add_everything_up(3.968, 'lao'))
print(add_everything_up('ierj', 34))
print(add_everything_up('ierj', 'jdh'))

