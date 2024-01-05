# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.


str1=input("ENter String: ")
a1=str1.find("not")  
a2=str1.find("poor") 
if a1<12: 
    str2=str1.replace(str1[a1:a2+4],"good")  
    print(str2)
else:
    print(str1)