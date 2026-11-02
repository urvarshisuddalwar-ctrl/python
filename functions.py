# a = 121
# rev = 0
# copy = a
# while a != 0:
#     rev = rev * 10 + a%10
#     a = a//10

# if copy == rev:
#     print("palindrome")
# else:
#     print("not a paliondrome")

# #user defined a funv=ction
# def hello():
#     print("how are you")

# #calling a function
# hello()

# #return

# def hey():
#     return "how are you" #return the value to
#                         #the calling block

# a =  hey() #calling block captures the value
# print(a)

# #parameters & arguments

# def addition(a,b): #you accept the parameters
#     print(a +b)

# addition(10,20) #and you provide the 
#                 #arguments to the parameters
# addition(50,50)

# def paliondrome(a):
#   rev =0
#   copy = a
#   while a != 0:
#      rev = rev * 10 + a%10
#      a = a//10

# if copy == rev:
#     print(copy)


# for i in range(1,1000):
#     paliondrome(i)

# #default parameters

# def hello(a,b,c,d,e=30):
#     print(a+b)
# #hello(50,50,20,56)

# #default arguments

# def information(name,age,number):
#     print("hello your info is")
#     print(name)
#     print(age)
#     print(number)

# information(number = 9907554321,name ="harsh",age =25)
# information()



# #print numbers from 1-30
# #you cannot use for and while loop
# #you cannot uses print statement more than 1.

# #recursion -a function calling function itself
# def numbers(n):
#     if n ==31:
#         return
#     print(n)
#     numbers(n+1)

# numbers(1)


def numbers(n):
    if n == 31:
        return
    numbers(n+1)
    print(n)

numbers(1)


 







 







 
