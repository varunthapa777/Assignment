mytuple = (3,4,5,1,10,16)

n = int(input("Enter element to find: "))

if n in mytuple:
    print(f"Element in {mytuple.index(n)} index")
else:
    print("Element found")