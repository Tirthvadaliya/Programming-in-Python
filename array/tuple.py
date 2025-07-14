mytuple=("hii","this is simple tuple",3,4,True,False) 
# Simple tuple 
print(mytuple) 
print("*******************************")
# Accessing tuple elements
print(mytuple[1])
print(mytuple[3]) 
print(mytuple[4])
print("*******************************")

'''Once a tuple is created, you cannot change its values.
Tuples are unchangeable, or immutable as it also is called.
'''
for x in mytuple:
    print(x)  # prints each element of the tuple
print("*******************************")

#join two tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)