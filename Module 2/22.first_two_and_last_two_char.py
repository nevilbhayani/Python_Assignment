# write a python program to get a String.if the string made of the first 2 and the last 2 chars from given a string. if the string length is less then 2, return instend of the empty string


def string(s):
    if len(str) <= 2:   
        print(" \n string is empty") 
    else:       
        print(str[:2] + str[-2:])
str=input("Enter a string :")
string(str)