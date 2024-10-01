immutable_var = 1, "a", True
print(immutable_var)

# immutable_var[0] = 2
# Попытка изменить значение в кортеже вызовет ошибку.
# Кортеж не поддерживает возможность внесения изменений, потому как является неизменяемой коллекией

mutable_list = [1, "a", True]
mutable_list[0] = "char"
mutable_list[1] = "b"
mutable_list[2] = False
print(mutable_list)