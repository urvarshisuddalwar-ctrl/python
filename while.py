# """"""
# WHILE LOOP
# kaha se jana hai -> kab tak jana hai

# while jab tak yeh condition true hai:
#       tab tak yeh code chalega
# """"""   

#1-50 tak print krna hai using while loop

# n= 1234
# a = 0
# while n > 0:
#     last = n % 10
#     a =a*10 + last
#     n = n // 10
# print(a)


#number kitne digit ka hai

# n =1234
# count = 0
# while n > 0:
#     last = n % 10
#     count =count + 1
#     a = a*10 + last
#     n =n // 10

# print(a)
# print(count)


#que1. number is armstrong or not .
n =153
sum = 0
temp = n
length = len(str(n))


while n > 0:
    last = n% 10
    sum = sum + last**length
    n = n // 10

if sum == temp:
    print(f"{temp} is armstrong number")
else:
   print(f"")


















 
     
     





