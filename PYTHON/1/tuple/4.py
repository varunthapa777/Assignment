def countOccurrence(t1,x):
    count = 0
    for item in t1:
        if(item == x):
            count += 1
    return count

myTuple = (1,1,2,2,6, 2, 2, 6)

print(countOccurrence(myTuple, 2))