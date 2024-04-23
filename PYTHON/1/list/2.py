def removeDuplicate(l):
    newList = []
    for item in l:
        if item not in newList:
            newList.append(item)
    return newList


listWithDuplicate = [1,5,6,6,1,3,2,2]

newList = removeDuplicate(listWithDuplicate);

print(newList)

