# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5 


def number(x, y):

    if x == y or (x - y) == 5 or (x + y) == 5:
        return True
    else:
        return False


print (number(7, 2))
print (number(5, 5))
print (number(2, 2))
print (number(7, 3))
print (number(27, 53))
