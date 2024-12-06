first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(string) for string in first_strings if len(string) >= 5]
second_result = [(s1, s2) for s1 in first_strings for s2 in second_strings if len(s1) == len(s2)]

third_strings = [*first_strings, *second_strings]
third_result = {string: len(string) for string in third_strings if len(string) % 2 == 0}
print(first_result)
print(second_result)
print(third_result)
