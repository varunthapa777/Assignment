def concatTuple(t1, t2):    
    return (*t1,*t2)


t1 = (1,2,3,4,5)
t2 = (4,5,3,5,1)

t3 = concatTuple(t1, t2)

print(t3)