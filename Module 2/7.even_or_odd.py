# Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user


num=int(input("Enter one number :"))
if (num % 2 == 0):      
    print(num,"number is Even")
elif (num % 2 != 0): 
    print(num,"number is odd")
else:
    print("Enter valid input")  
