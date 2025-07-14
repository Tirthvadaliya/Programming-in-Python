import array as arr

# creating array of integers
a = arr.array('i', [1, 2, 3])

# accessing First Araay
print(a[0])

# Adding element to array
a.append(5)
print(a)

# print the type code
print(a.typecode) # i for integer