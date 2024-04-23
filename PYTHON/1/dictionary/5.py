
# Write a program to sort a dictionary by its values in ascending order

def sort_dict_by_values(dictionary):
    sorted_dict = sorted(dictionary.items(), key=lambda x: x[1])
    return dict(sorted_dict)


my_dict = {'apple': 2, 'banana': 1, 'orange': 3, 'pear': 2}
sorted_dict = sort_dict_by_values(my_dict)
print(sorted_dict)

