import sys
my_dict = {'a': 10, 'b': 7, 'c': 15, 'd': 4}


max_value = max(my_dict.values())
max_key = [key for key, value in my_dict.items() if value == max_value]


min_value = min(my_dict.values())
min_key = [key for key, value in my_dict.items() if value == min_value]


print(f"Key with maximum value: {max_key}")
print(f"Key with minimum value: {min_key}")

