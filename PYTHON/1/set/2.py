def have_intersection(set1, set2):
  # Check if the intersection of the sets is empty
  return not set1.isdisjoint(set2)


set1 = {1, 3, 5, 7}
set2 = {2, 4, 6, 8}

# Check if the sets have any elements in common
has_common = have_intersection(set1, set2)

if has_common:
  print("The sets have at least one element in common.")
else:
  print("The sets have no elements in common.")
