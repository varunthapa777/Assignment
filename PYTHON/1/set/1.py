set1 = {1, 3, 5, 7}
set2 = {2, 4, 6, 8, 1}


print("Set 1:", set1)
print("Set 2:", set2)


union = set1.union(set2) # | union
print("Union:", union)

intersection = set1.intersection(set2) # & intersection
print("Intersection:", intersection)

difference = set1.difference(set2) # - difference
print("Difference (Set 1 - Set 2):", difference)


difference = set2.difference(set1)
print("Difference (Set 2 - Set 1):", difference)