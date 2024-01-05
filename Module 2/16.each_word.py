# Write a Python program to count the occurrences of each word in a given sentence


n=input("Enter a sentence: ") 
dict1={}  
words=n.split()    
n=1
for i in words:  
    if i in dict1.keys():
        dict1[i]=n+1   
    else:
        dict1[i]=n   
print(dict1)