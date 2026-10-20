# Write a Python program to check whether the n-th element exists in a given list.


list=[1,2,4,6,8,10]
print(list)
n=int(input("enter the element to check it is in the list :"))
for i in range(len(list)):
    if n==list[i]:
        print("yes it in the list")
        break
else:
    print("it is not in the list")
    

