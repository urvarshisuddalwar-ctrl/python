#TUPLE

# 1. Annoted by (paranthesis)
# 2. Tuples are ordered.
# 3.Tuples are Immutable.
#4. Tuple can store duplicate values.
#5. Hetrogenous -> can store mixed type of data.
""
# t= () #Empty Tuple
t = (1,2,3,4, "Hello", 7.32,True)





#MEHODS OF TUPLE

#1..index() -> return index of any value.
#2. .count() -> count occurence of any value
""
# print(count[1])
""

#OPERATIONS

# +  -> concatenation
#  * -> Repetition
# ""
# t1 =(1,2)
# t2 = (3,4)
# print(t1 +t2)
# print(t1 *5)

t =(1,2, [3,4,5])
t[2].append(100)
print(t)



t =(1,2,3,4,5)
for i in range(len(t)):
    print(i, t[i])

