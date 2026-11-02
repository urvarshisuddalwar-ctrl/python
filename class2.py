# # # variables -- ctrl + ? 
# # name = "urvashi"
# # age=18
# # print(name,age)
# # # print(age)

# # # data types 
# # # 1. numeric / numbers 
# # # a. int 
# # age=19
# # marks=78
# # salary=50000
# # # print(age , marks ,salary)
# # print(type(marks))

# # b. float -->> decimal values or p/q
# # a=12.20
# a=       20
# b=5
# print(a)


# # c. complex 
# num=8j
# print(type(num))


# # 2. string  -->> anything written inside "" or '' is known as strings
# n="            hi "
# print(n)

# slicing and indexing 
# slicing -->> whenever u want to access any single or particular value of a string 
# indexing of string starts from 0
# positive indexing  -->> moving in forward direction : 0,1,2,3,4
# s="python"
# print(s[0])
# print(s[3])
# print(s[5])

# # negative indexing -->> moving from backward direction -1,-2,-3,-4,... 
# s="python"
# print(s[-1])
# print(s[-5])

# slicing --> it means taking any particular part of string 
# syntax -->> s[start index : stop index: step value ] stop value+1
# s="sheryians"
# print(s[0::3])
# print(s[0:4:1])
# print(s[0:4:2])

# print(s[-1:-5:-1])
# print(s[0::1])
# print(s[-1::-1])

# 3.boolean --> True or False
# print(bool(0))  -->> bool() is used to check whether a value is true or false

# here below are 7 values which are considered as falsy values and all other than these are known as truthy values 
# print(bool(0))
# print(bool(0.0))
# print(bool(False))
# print(bool(""))
# print(bool([]))
# print(bool(()))
# print(bool({}))
# print(bool(12))


# operators 
# 1. Arithmetic operators  +,-,/,*,%,//,**
# a=2
# b=3
# print(a+b)
# print(a-b)
# print(a/b)
# print(a*b)
# print(a%b)
# print(a//b)
# print(a**b)

# comaparision operators
# ==,>=,<=,<,>
# a=10
# b=20
# print(a==b)
# print(a>=b)
# print(a<=b)
# print(a<b)
# print(a>b)


# assignment operators
# +=,-=,/=,*=,//=,%=,**=
# a=10
# # a+=10
# # print(a)
# a-=10
# print(a)
# a*=10


# logical operators 
# and , or , not 
# 1. and -- if we want true as an output so all conditions should bne true 
# if any one of the conditions is false then it will give false an an output
# print(10<20 and 20>15 and 1<12 and 2>1 and 10==10 )


# # or  -> if any one condition is true it will give true 
# print(10>20 or 20<15 or 1>12 or 2<1 or 10==1 )

# # not--> it just reverse the output 
# print(not(10<20 or 20<15 or 1>12 or 2<1 or 10==1 ))


# num=int(input("enter your number : "))
# if num==100:
#     print("you have 100 rupees to spend")
# elif num==500:
#     print("you have 500 rupees to spend")
# else: 
#     print("you have got fake note")===========

#
# = 5
#num2 = 3

print("num1 + num2")
print("num1 % num2")

num1 =3
num2=6
print(num1**num2)
print(num1 -num2)


# num1=5
# num2=6
# print(num1*num2):

#num1=20
#num2=4
#print(num1/num2)

maths =input("enter maths")
# science =int(input("enter marks of science "))
# eng=int(input("enter marks of eng"))
# if maths=40 and science =40 and eng =40
#    print =("pass")

a =int(input("enter first number"))
b=(input("enter second number"))
c=(input("enter first number"))

# if  a==b and b==c and a==c:
#     print("all the equal")
# elifa==b
# print("any two number are equal")
# else
#     print("all are different")

# if num==0
# print("number is zero")
#elifnum>0 and num%2==0
#print("+even")
# elif num>0 and num%2!=0
num1

if num>=0:
    print("num is +")
    if num>=10:
       print("and num> 10")
else:
    print("and num< 10")
print("num is -")


num =int(input("enter the num"))   

if num%2==0:
   if num%4== 0:
      print("num is even and div by 4")
   else:
      print("num is even and not div by4")
else:
   print("num is odd")  


pin =int(input("enter the pin"))

if pin == 1234:
   amount =int(input("enter the amount to withdraw"))
   if amount <=5000:
      print("withdraw done")
   else:
      print("garib ho aap")   
else:
   print("chor ho aap") 


num =(input("enter the num")) 

if num>=0:
    print("num is +" )
    if num%2==0:
        print("num is even")
    
    if num%4==0:
        print(" div by 4")
    else:
       print(" not div by 4") 
else:
 print("and odd")
print ("num is -")
if a>=b:
   print("")