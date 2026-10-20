#Write a Python function that accepts a string and counts the number of upper- and lower-case letters.
def upper_lower(s):
    upper=0
    lower=0
    for i in s:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
    return upper,lower

string=input("enter the string")
upper,lower=upper_lower(string)
print("upper case",upper)
print("lower case",lower)


