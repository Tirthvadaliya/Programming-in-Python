thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
print(thisdict)
print(thisdict["model"]) 
print(thisdict["year"]) 

print(len(thisdict)) # returns total number of items in a dictionary


print("*******************************")
#Note: The values in dictionary items can be of any data type:-
#String, int, boolean, and list data types

thisdict2 = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict2)
print(thisdict2["colors"]) 

print("*******************************")
print("Change value of 'year' to 2018:")
print("before change: ", thisdict2["year"])
thisdict2["year"] = 2018
print("after change: ", thisdict2["year"])


print("*******************************")
print("ADD New value:")
print("before ADD: ", thisdict2["year"])
thisdict2["color"] = "red"
print("after ADD: ", thisdict2["year"])


print("*******************************")
print("Delete particular value in dictionary:")
print("before Delete: ", thisdict2)
thisdict2.pop("color")
print("after Delete: ", thisdict2)

print("Delete All values in dictionary:")
print("before Delete: ", thisdict2)
print("after Delete: ", thisdict2.clear())


