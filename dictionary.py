""""""
# DICTIONARY
# 1. Dictionary Annoted by {curly brackets}
# 2 Dictionary are combination of multiple keys:values
#3.Dict are mutable.
#4.Dict are Hetrogenous
# 5.In Dict Keys will be UNIQUE  but Values can be  DUPLICATE.
#6.In Dict keys can't be Duplicate but Values can be Duplicate.
""""""

# d ={1:10,2:20,3:30}
# d[4] =100 #creating a new key:value pair which never exists.
# print(d)


d ={1:10, 2:20,3:20}
print(d)

d ={1:10, 2:20,3:20}

for i in d:#i->1
    print(i,d[i])#1, d[1]

#Methods IN DICT.
#1. .KEYS()
D = {"ravi" : 80, "Rohan": 23, "Devraj":88}
print(d.keys)

#2. .Values()
print(d.values())

#3..items() -> both keys and values 
print(d.items())

#4. .pop ()-> key and emove both key and value.
d.pop("Rohan")
print(d)

#5..get() -> agar key present hai in dictionary so we will get value for that key either wise NONE or any MESSAGE
print(d.get(5, "NOT Found"))

# .update() -> merge two dictionaries.
a ={1:10,2:20,3:30}
b = {3:40,5:50 ,6:60}
a.update(b)
print(a)

#que.print keys
d ={"Ravi": 70, "Abhishek":33, "Rohan":12}


#Method -1
print(d.keys())

 #Method -2
for i in value :


#Methods -3
for  key,Value in d.items():   
    print(key)




#Que. find the total of marks without using SUM()
d= {"Ravi": 70,"Abhishek":33, "Rohan":12}

total = 0
for i in d.values():#i->70
    total = total +i

print(total)


#que. print student name who scored more than 50
d = {"Ravi":70, "Abhishek":88, "Rohan":12}

for name, marks in d.items()#name="Ravi",marks=70
    if marks >=50:
        print(name)

#Que. find the atudent with the highest marks.
d = {"Ravi":70, "Abhishek":88, "Rohan":12}

highest=0
for name, marks in d.items():
    if marks > highest:
        highest = marks
        top = name
        print(top,highest)


#Que. Add Bonus 5 marks to every student.
d ={"Ravi":70, "Abhishek":88, "Rohan":12}

for i in d:
    d[i] =d[i] + 5

print(d)







    









