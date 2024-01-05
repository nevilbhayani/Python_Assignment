# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string

a =input("Enter string a :")    
b =input("Enter string b :")     
print("Before Swap :",a,",",b)   
a1=a[1]+a[0]+a[2:]       
b1=b[1]+b[0]+b[2:]   

print("After Swap :",a1,",",b1)