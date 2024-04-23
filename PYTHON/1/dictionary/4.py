def isKeyExist(d1, key):
    if key in d1.keys():
        return True
    return False

my_dict = {'a': 10, 'b': 7, 'c': 15, 'd': 4}

print(isKeyExist(my_dict, 'a'))
print(isKeyExist(my_dict, 'h'))