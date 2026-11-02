# present = 0
# absent= 0

# for i in range(1 ,8):
#     status = input("enter 1 for Passed and 0 for fail: ")

#     if status == "P":
#         present += 1
#     elif status == "A":
#         absent += 1
# print("Total present days =",present)
# print("total absent days =",absent) 


# passed =1
# failed =0

# for i in range(1, 11):
#     product = int(input("enter 1 for passed and 0 or fail:"))

#     if product == 1:
#        passed +=1
#     elif product == 0:
#         failed += 1
#     print("passed products =", passed)
#     print("fail products =",failed)

#     total =0
#     count =0

#     for i in range(1,8):
#         amount=int(input("enter savings: "))
#         total= total+ amount

#         if amount is>500:
#            count =count+1
#     print("total savings")


# #factorial

# n = int(input("enter the num"))
# fact =1
# for i in range 




# #strong number

# n = int(input("enter the number"))
# sum = 0
# while n >0:
#     digit =n%10
#     #digit/
#     f_of_digit=1




# n = int(input("entewr the number"))

# for i in range(1,n+1):
#     if i %2!=0:
#         sum+=i
# print(f"sum of odd numbers from 1 to {n} is {sum}")


      




# #user ki attempts ke andqar pin check karna hai
# # # user se pin check karana hai in limits ->pin real ==pin input
# #  -> incorrect
# # ->1st time and 2nd -> pin is incorrect ->chance dena again
# # ->3rd time ->incorrect -> cxard blocked chor ho aap
# # 1st and 2nd and 3rd ->correct -> main menu and chance step




# #input ahould be taken when user have leftout attempts
# attempts =3
# while attempts > 0:
#     entered_pin =int (input("enter the pin"))
#     if entered_pin ==1234:
#         #main menu opens
#         pass
#     else:
#         attempts -=1
#         if attempts ==0:
#             print(f"incorrect pin! you have{attempts} attempts remaining")
#         else:
#             print("card blocked")

              


# #dictionary

# **Q1. Create a Dictionary**

# Create a dictionary containing your name, age, and city. Print the dictionary.

# **Example Output:**

# {'name': 'Rahul', 'age': 20, 'city': 'Bhopal'}



# d ={}

# d['name'] = 'Rahul'
# d['AGE'] = '20'
# d['City'] = 'bhopal'

# print(d)


# Q2. Access a Value**

# Given a dictionary, print the value associated with the key "name".

# **Example:**

# - Input: {'name': 'Rahul', 'age': 20, 'city': 'Bhopal'}
# - Output: Rahul**



# d ={'name': 'Rahul', 'age': 20, 'city': 'Bhopal'}

# print(d['name'])


# # **Q3. Add a New Key-Value Pair**

# # Add a new key "course" with value "Python" to the given dictionary.

# # **Example:**

# # - Input: {'name': 'Rahul', 'age': 20}
# # - Output: {'name': 'Rahul', 'age': 20, 'course': 'Python'}


# d  ={'name': 'Rahul','age':20}
# d['course'] = 'python'
# print(d)

# # **Q4. Update a Value**

# # Update the age of a person to 21.

# # **Example:**

# # - Input: {'name': 'Rahul', 'age': 20}
# # - Output: {'name': 'Rahul', 'age': 21}


# person = {'name':'Rahul','age':20}
# person['age'] =21
# print(person)



# # **Q5. Delete a Key**

# # Remove the key "city" from the dictionary.

# # **Example:**

# # - Input: {'name': 'Rahul', 'age': 20, 'city': 'Bhopal'}
# # - Output: {'name': 'Rahul', 'age': 20}


# person = {'name':'Rahul', 'age':20,'city':'Bhopal'}
# del person['city']
# print(person)


# # **Q6. Check if a Key Exists**

# # Check whether the key "age" exists in the given dictionary.

# # **Example:**
# # - Input: {'name': 'Rahul', 'age': 20}
# # - Output: Key exists

# person = {'name':'Rahul','age':'20'}

# if 'age' in person:
#     print("key exists")
# else:
#     print("key does not exists")

# # **Q7. Print All Keys**

# # Print all the keys present in a dictionary using a loop.

# # **Example:**

# # - Input: {'name': 'Rahul', 'age': 20, 'city': 'Bhopal'}
# # - Output:
# # name
# # age
# # city

# person ={'name': 'Rahul', 'age': 20,
# 'city': 'Bhopal'}
# for key in person:
#     print(key)

# **Q8. Print All Values**

# Print all the values present in a dictionary using a loop.

# **Example:**

# # - Input: {'name': 'Rahul', 'age': 20, 'city': 'Bhopal'}
# # - Output:
# # Rahul
# # 20
# # Bhopal

# person = {'name': 'Rahul', 'age':  20, 'city': 'Bhopal'}
# for values in person.values(): 
#     print(values)

# # **Q9. Count Key-Value Pairs**

# # Count the total number of key-value pairs in a dictionary without using len().

# # **Example:**

# # - Input: {'a': 10, 'b': 20, 'c': 30}
# # - Output: 3


# data  = {'a': 10, 'b':20, 'c':30}
# count = 0
# for key in data:
#     count = count + 1
#     print (count)

# **Q10. Calculate the Sum of Values**

# Calculate the sum of all numerical values in a dictionary using a loop.

# **Example:**

# - Input: {'a': 10, 'b': 20, 'c': 30}
# - Output: 60

data ={'a': 10, 'b': 20, 'c':30}
total = 0

for value in data.values():
    total = total + value
    print (total)  































