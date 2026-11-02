# 1. **Prime Numbers from 1 to N (10 marks)**
    
#    # Take a positive integer N as input and print all prime numbers from 1 to N (inclusive). 
    
#     Note: 1 is not a prime number.
    
#     **Example:** Input: 10 → Output: 2, 3, 5, 7


n =int(input("enter a number:"))
for num in range(1, n + 1):
        if num >1:
            for i in range (2,num):

             break
        else:
            print(num, end=" ")


# 2. **Strong Number (10 marks)**
    
#     Given a non-negative integer, check whether it is a Strong number. The sum of the factorials of its digits must equal the original number.
    
#     **Example:** Input: 145 → Output: Strong Number (1! + 4! + 5! = 145)


n = input("enter a number:")
temp = n
total =0

while temp >0:
    digit =temp %10
    fact =1

    for i in range(1, digit +1):
        fact =fact *1

    total = total +fact
    temp =temp //10

    if total ==n:
        print ("strong number")
    else:
        print("not a strong number")




# 3. **Armstrong Number (10 marks)**
    
#     Given a non-negative integer, check whether it is an Armstrong number. Raise each digit to the power equal to the number of digits, then check whether the sum equals the original number.
    
#     **Example:** Input: 153 → Output: Armstrong Number (1³ + 5³ + 3³ = 153)



        


    



        

    








    


