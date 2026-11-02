""
# SETS
1#stores only unique elements and removes duplicate ones.
2.# Sets are annoted by{} or set()
3.#Sets are unordered that means there is no indexing in sets.
4.#Sets are Hetrogenous.
5.#Sets are semi-mutable
""
s = set()#EMPTY 
s  ={1,1,2,2,3,4,5,70.2,"Sample"}
print (type(s))

""

#LIST to SET
l =[1,2,3,4,5]
print(set(l))




""

#SET METHODS.
1.#add()-> add element to set
S ={1,2,3,4}
S.add(5)


#2.remove() -> remove an element if the element didn't exists we will get an KEYERROR
S.remove(100)
print(s)

#3. .discard() -> will not show any error if the element is not present in set.
s.discard(100)
print(s)



#set operations
""


s1 ={1,2,3,4}
s2 ={4,5,6,7,8}

#1. .union
#merge both the elements
print (f"UNION -> {s1. union(s2)}")
""
s1 = {1,2,3,4}
s2 = {4,5,6,7,8}
print(f"UNION ->{s1 | s2}")

2.# INTERSECTION
#Common elements.

s1 ={1,2,3,4}
s2 ={4,5,6,7,8}
print(f"INTERSECTION -> {s1.intersection(s2)}")

s1 = {1,2,3,4}
s2 = {4,5,6,7,8}
print(f"INTERSECTION -> {s1 & s2}")

3. .difference()
#Elements present in one set but not in another
""
s1 ={1,2,3,4}
s2 ={4,5,6,7,8}
print(f"DIFFERENCE -> {s1. difference(s2)}")
print(f"DIFFERENCE -> {s2.difference(s1)}")

s1 = {1,2,3,4}
s2 = {4,5,6,7,8}
print(f"DIFFERENCE ->{s1 -s2}")


4. .symmetric_difference()
""
s1 = {1,2,3,4}
s2 = {4,5,6,7,8}
print(f"SYMMETRIC ->{s1. symmetric_difference(s2)}")

s1 = {1,2,3,4}
s2 = {4,5,6,7,8}
print(f"SYMMETRIC -> {s1 ^s2}")



s ={}
s =set()

#FROZENSET makes any set with of fixed elements we cannot add element and we cannot remove one.
s = frozenset([1,2,3,4,5])
s.add(6)
print(s)










