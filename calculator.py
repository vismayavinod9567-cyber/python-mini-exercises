
def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def division(x,y):
    return x/y
def multiplication(x,y):
    return x*y
print("A : Addition")
print("B : subtraction")
print("C : division")
print("D : multiplication")
choice=input("enter your choice :")
n1=int(input("enter your first number :"))
n2=int(input("enter your second number :"))
if choice=="A" or choice=="a":
    print(addition(n1,n2))
elif choice=="B" or choice=="b":
    print(subtraction(n1,n2))
elif choice=="C" or choice=="c":
    print(division(n1,n2))
elif choice=="D" or choice=="d":
    print(multiplication(n1,n2))
else:
    print("you entered a invalid choice")

