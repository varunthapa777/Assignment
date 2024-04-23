def isCommon(t1, t2):   
    for item in t1:
        if item in t2:
            return True
    return False


t1 = (1,2,5,3,7)
t2 = (6,7,10, 9, 1)
t3 = (6,10, 9)

print(isCommon(t1, t2))
print(isCommon(t1, t3))