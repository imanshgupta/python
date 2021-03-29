months = {"jan", "feb", "mar", "april", "june", "july", "aug"}
set1 = set()
set1 = {1, 2, 3, 4, 5, "hellow", "hi", "adios", "bye", "jan", "feb"}
print(set1.__sizeof__())
set1.add("hknkni")
print(set1)
# to remove but if noot found then errror occurs
set1.remove("hi")
# tto remove but if element is not found then no error
set1.discard("hi")
print(set1)
# removing an element at random
set1.pop()
set1.pop()

# union
set5 = set1.union(months)
# union other way
set5 = set1 | months
print(set5)
# intersection
set6 = set1.intersection(months)
# another intersection method
set6 = set1 & months
print(set6)
# minus of two sets
set7 = set1-months
print(set7)
# to do symmetric differnece
set8 = set1.symmetric_difference(months)
print(set8)
# another method to do symmetric difference
set9 = set1 ^ months
# to clear the contents of a set

# set1.clear()
# print(set1)

# to add to any set
set1.update(months)
print(set1)
# to take intersecton and add to another set
set1.intersection_update(months)
print(set1)
