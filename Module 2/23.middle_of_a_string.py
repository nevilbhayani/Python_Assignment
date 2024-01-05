# Write a Python function to insert a string in the middle of a string


def string(a,b):
    return a[:2] + b + a[2:]
str1=(input("Enter a string A :"))
str2=(input("Enter a string b :"))
print(string(str1,str2))