#data structures.
#list
#1.square brackets -> list[]
#2.hetrogenous data structures (a list can store different  data types together)
#3.List allows storing duplicate values.
#4.List are ordered - because they have indexing and indexing starts from 0.
#5.list are Mutable -> we can change any value anytime and anywhere.
#marks =[] #empty list 
marks=[80,78,90,  "Sheryians",3.14]
marks[3] = "Modiji"
print(marks[3])



# #Traversing
# a =[10,20,30,40,50]
# for i in a: 
#     print(i)

# #agar kisi keyword ke dot ni laga toh wo ek function h print()




# #.append
# #methods in list
# #1. .append() add the value at the last of list.
# marks =[10,20,30,40,50]
# marks .append(90)
# print(marks)

# #2. .extend()
# marks2 = [70,80,90]
# marks2.extend(marks2)
# marks.extend(marks)
# print(marks2)

# #3. .insert(index, value)
# marks.insert(3, 90)
# print(marks)


# #4.remove() -> remove any value from the list.
# a = [10,20,30,40,50]
# a.remove(10)
# print(a)

# #5. .pop() -> remove any value basis on the index.
# a =[10,20,30,40,50]
# a.pop(3)
# print(a)

# #6. .clear() -> removes all the element and gives empty list.
# a =[10,20,30,40,50]
# a.clear()
# print(a)

# #7. del -> removes list from the memeory.
# # a =[10,20,30,40,50]
# # del a
# # print (marks)
# # print(a)

# # Shallow copy

# a =[1,2,3,4,5]
# b = a.copy() #Deep copy
# b[3] = 100
# print(a)
# print(b)

# l =[10,20,30,40,50,60,70,80]
# for i in l:
#     print(i)

# l =[10,20,30,40,50,60,70,80]
# for i in range(len(l)):
#     print(i, l[i])

# l =[10,20,30,40,50,60,70,80]
# for i in range(len (l)-1,-1,-1):
#     print(l[i]) 


# a =[10,20,30,40,50,60,70,80]
# l2 =[]#[80,70,60,50,40,30,20,10]

# for i in range(len(l)-1,-1,-1):
#     l2.append(l[i])
#     # l2.insert(len(l2),l[i])
# print(l2)


# #reverse

# arr = [10,20,30,40,50]
# n = len(arr)
# mid = n//2
# for i in range(mid):
#     arr[i] , arr[n-i-1] = arr[n-i-1] , arr[i]



# arr =[10,-5,20,40,-3,0,8]

# print("positive:")
# for elem in arr:
#     if elem>0:
#         print(elem)


# print("negative")
# for elem in arr:
#     if elem<0:
#         print(elem)

# #Mean of List Elements
# #
# #calculate the average of all elements in a list.
# #example:
# #input: [10,20,30,40]
# #output:mean =25.0


# list =[10,20,30,40]
# n = len(list)
# sum =0
# for elem in list:
#     sum+=elem
# print(f"mean is {sum/n}")



# arr =[2,96,69,77,145,20]
# max =arr[0]
# index =0
# for i in range(len(arr)):
#     elem =arr[i]
#     if elem > max:
#         max =elem
#         index = i

# print(f"max is {max} at index {index}")



# arr = [1,2,4,5]
# n = len(arr)
# og_n = n+1
# og_sum =((og_n)*(og_n+1)) //2
# real_sum =0
# for elem in arr:
#     real_sum +=elem

# missing= og_sum -real_sum
# print(missing)


# arr = [10,20,30,40,50]
# is_sorted = True
# n = len(arr)
# for i in range(0,n-1):
#     if arr[i] > arr[i+1]:
#         is_sorted = False
#         break

#     if is_sorted:
#         print("list is sorted")
#     else:
#         print("list is un sorted") 





# arr = [2, 3, 15, 3, 2]
# n = len(arr)
# is_palindrome = True
# for i in range(n//2):
#     if arr[i] !=arr[n-i+1]:
#         is_palindrome = False
#         break
# if is_palindrome:
#     print("list is palindrome")
# else:
#     print("not palindrome")


#bubble shot

arr =[64,34,25,12,22,11,9]
n = len(arr)
for i in range(n):
    for j in range(n- i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1] , arr[j]

print(arr)


#selection shot

 



























































