# Write a Python program to get the Fibonacci series of given range




n = int(input("Enter a number: "))  # usar input
print(f"fibonacci num is {n}")   # print input number
n1=0
n2=1
n3=0
print(n1,n2,end=" ")        
for i in range(2,n):    
    if (n<=1):
        print(1)
    else:
        n3=n1+n2      # else logic fibonacci 
        n1=n2 
        n2=n3
        print(n3,end=" ")