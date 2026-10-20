#Python program to print the duplicate elements of an array
array1=[1,2,7,2,3,33,33]
newlist=[]
for i in range(len(array1)):
    for j in range(i+1,len(array1)):
        if array1[i]==array1[j] not in newlist:
            newlist.append(array1[i])
print(newlist)
