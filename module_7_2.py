def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding='UTF-8')
    strings_positions = {}
    current_line = 0
    for string in strings:
        current_line += 1
        byte_index = file.tell()
        file.write(string + '\n')
        strings_positions[(current_line, byte_index)] = string

    file.close()
    return strings_positions

info = ['Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!']
result = custom_write('test', info)
for elem in result.items():
    print(elem)