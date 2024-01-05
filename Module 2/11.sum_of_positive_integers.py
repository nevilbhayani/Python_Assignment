# Write a python program to sum of the first n positive integers

num=int(input("Enter number one num  :"))
sum = 0   
for i in range(1,num+1):
    sum = sum + i    
print("sum is :",sum)