def findMax(l):
    max = l[0]
    for i in l:
        if i > max:
            max = i
    return max

def findMin(l):
    min = l[0]
    for i in l:
        if i < min:
            min = i
    return min

myList = [1, 2, 0, 90, 50]

print(findMax(myList))

print(findMin(myList))