num=int(input("enter the number :"))
if num<0:
    print("please enter a positive number :")
elif num==1:
    print("u entered a composite number ")
else:
    for i in range(2,1,num):
        if num%i==0:
            print(f"{num} is a not prime number")
            break
    else:
        print(num,"is a prime number")
