my_dict = { "Michail" : 2000, "Denis" : 1995, "Alex" : 1999 }
print(my_dict)

print(my_dict["Alex"])
print(my_dict.get("Vanya"))

my_dict["Vanya"] = 1989
my_dict["Masha"] = 1996

my_value = my_dict.pop("Alex")

print(my_value)
print(my_dict)

my_set = { 2, True, 2.0, False, "Michail", 5, 2, True, False, "Vanya", "Michail" }
print(my_set)

my_set.add(666)
my_set.add("Dracula")

my_set.remove(5)
print(my_set)