# Write a Python function that takes a list of words and returns the length of the longest on



def longstest(str1):
    word=str1.split()  
    long=len(word[0])     
    for i in word:  
        if long < len(i):    
            long=len(i)     
            print("largest string of length :",{long})       

            
str1=input("Enter line of string :") 
longstest(str1)  

