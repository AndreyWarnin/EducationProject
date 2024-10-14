def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()

def is_contains(string, list_to_search):
    count_calls()
    string = str.lower(string)
    contains = False
    for s in list_to_search:
        s = s.lower()
        if s == string:
            contains = True
            break
    return contains

calls = 0
print(string_info('OPERAtion'))
print(string_info('Joy'))
print(string_info('Joy'))
print(is_contains('OPERAtion',
                  ['Operation', 'Gravity']))
print(is_contains('Joy',
                  ['jooy', 'Nickname', 'Joyy', 'jo']))
print(is_contains('Joy',
                  ['oy', 'Simple', 'joY', 'Marble']))
print(calls)