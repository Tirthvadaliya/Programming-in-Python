a = [1, "Hello", [3.14, "world",2,3,9],5]
a.append(2)  # Add an integer to the end
print(a[1]) # prints: Hello
print(a[2][1]) # Output: world
print(a[2][4]) # Output: 9
print(a[3]) # Output: 5

print("**********************")

mylist = ["apple", "banana", "cherry"]
print(type(mylist))
print(mylist[2])

print("******************")
#change list
mylist[1] = "blackcurrant"
print(mylist)

print("******************")
# add item
mylist2 = ["apple", "banana", "cherry"]
mylist2.insert(1, "orange")
print(mylist2)


#remove item
mylist2.remove("banana")
print(mylist2)

#loop through list
print("******************")
print("loop through list")
mylist2 = ["apple", "banana", "cherry","mango","orange","kivi"]
for x in mylist2[::2]:
  print(x)


#join list
print("******************")
print("join list")
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print("List1:-",list1)
print("List2:-",list2)
print("List3:-",list3)

#sort the list
print("******************")
print("sort list")
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
print("before sorting:-",thislist)
thislist.sort()
print("after sorting:-",thislist)


#reverse the list
print("******************")
print("reverse list")

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

print("List:-",thislist)
thislist.sort(reverse = True)
print("after reverse sort:-",thislist)