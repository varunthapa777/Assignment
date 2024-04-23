def mergeDict(d1,d2):
    return {**d1, **d2}

d1 = {"car": 4, "bike": 2}
d2 = {"truck": 8, "auto": 3}

d3 = mergeDict(d1, d2)

print(d3)