my_dict = {"Elena":2020, "Petr":2019, "Misha":1987, "Anna":1985}
print(my_dict)
print(my_dict["Misha"] , my_dict.get("Vasya"))
my_dict.update({"Nikita":1999, "Dima":2000})
print(my_dict)
a = my_dict.pop("Petr")
print(my_dict)
print(a)

my_set = {15, 25, 66, 'Anna', True, (1,2,3), 'Anna', (1,2,3), 66}
print(my_set)
my_set.add(7)
my_set.add(17)
my_set.remove('Anna')
print(my_set)
#



