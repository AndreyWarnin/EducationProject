def print_params(a=1, b='строка', c=True):
    print(f'{a} {b} {c}')

print_params(2, 3, False)
print_params(2, False)
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = ['0', 0.1, False]
values_dict = { 'a': 0, 'b': '0', 'c': False }
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)

values_dict = {'a':1, 'b':2}
print_params(**values_dict)