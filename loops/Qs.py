#print the elements of the following list using a loop:
num = [1, 4, 9,16, 25, 45,49,64,72, 81,100]

i =0
while i< len(num):
    print(num[i])
    i +=1

#search for a number x in this tuple using loop:

nums = (1, 4, 9,16,35,56,67,78,89,67,100)
x=67

i=0
while i<len(nums):
    if(nums[i] == x):
        print("found it", i)
        break
    else:
        print("finding")
    i +=1