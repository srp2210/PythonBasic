"""
Write a Python program to get the difference between a given number and 17, 
if the number is greater than 17 return double the absolute difference.
"""
num = int(input("enter number : "))

if num <= 17:
        print("num is ",(17-num))
else:
        print("num is",(num -17)*2)