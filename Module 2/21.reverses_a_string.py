# Write a Python function to reverses a string if its length is a multiple of 4.


def reverse(a):   
    if len(str1) %4==0:
        return str1[-1::-1]
    else:
        return str1
str1=input("Enter string:")    
reverse(str1)