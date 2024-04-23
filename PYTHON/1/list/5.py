def sortList(l):
    n = len(l)
    for i in range(n):
        for j in range(i + 1, n):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]


mylist = [3,6,1,3]

sortList(mylist)

print(mylist) 