def count(collection):
    counter = 0
    for element in collection:
        if isinstance(element, int):
            counter += element
        elif isinstance(element, float):
            counter += element
        elif isinstance(element, str):
            counter += len(element)
        elif isinstance(element, bool):
            counter += element
        elif isinstance(element, tuple):
            counter += count(element)
        elif isinstance(element, list):
            counter += count(element)
        elif isinstance(element, set):
            counter += count(element)
        elif isinstance(element, dict):
            counter += count(element.items())
    return counter

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(count(data_structure))