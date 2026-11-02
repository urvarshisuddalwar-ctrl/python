# arr =[1,2,3,4,5]
# k =2
# k =k%len(arr)
# for i in range(k):
#     last = arr .pop()
#     arr.insert(0,last)
# print(arr)

# arr =[1,2,3,2,4,1,5]
# n = len(arr)
# dupd = []

# for i in range (n):
#       count =1
# for j in range(i+1,n):
#           if arr[i] == arr[j]:
#              count+=1
             
# if  count >=2:
#      'dupd'.append(arr[i])        

# print(dupd)



"""
Question: Merge Two Sorted Lists Without Using sort()

Write a Python program to merge two sorted lists into a single
sorted list without using the sort() function or any Sorting Algo.

Example:
Input:
arr1 = [1, 4, 7, 10]
arr2 = [2, 3, 8, 9]

Output:
[1, 2, 3, 4, 7, 8, 9, 10]
"""

arr1 = [1, 4, 7, 10]
arr2 = [2, 3, 8, 9]

n1 =len(arr1)
n2 =len(arr2)

i =0
j =0
ans=[]
while i<n1 and j<n2:
      if arr1[i]<arr2[j]:
         ans.append(arr1[i])
         i+=1
      else:
           ans.append(arr2[j])
           j+=1
while i< n1:
      ans.append(arr1[i])
      i+=1
while j < n2:
    ans.append(arr2[j])
    j+=1
print(ans)




