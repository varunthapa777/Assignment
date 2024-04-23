myList = [10, 20 , 30, 40, 50, 60, 70]

n = len(myList)
revList = []
for i in range(n):
    revList.append(myList[n-i-1])

print(revList)