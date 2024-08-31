immutable_var = ("ball","basket","card",7,True)
print(tuple(immutable_var))

immutable_var[0]="icecream"
immutable_var[2]=10
# Кортежи это неизменяемая последовательность элементов, поэтому нельзя изменить значения элементов кортежа

mutable_list = ["monkey", "lion", "elephant", "zebra"]
mutable_list[0:4] = ["cat", "dog", "fox", 'tiger']
print(mutable_list)