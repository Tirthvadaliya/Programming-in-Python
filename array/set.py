myset={"apple", "banana", "cherry", True, 1, 2}
print(type(myset))
print(myset) 
print("*******************************")
thisset = {"apple", "banana", "cherry", 0,1,False, True}
print(thisset)#Note: The values False and 0 are considered the same value in sets, and are treated as duplicates.

print("*******************************")

for x in thisset:
  print(x) # Note: The order of items in a set is not guaranteed to be the same each time you

print("*******************************")
print("Add Item in Set")

print("before add element the set=",thisset)
thisset.add("orange")
print("after add element the set=",thisset)


print("*******************************")
print("Join Set's")
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)
