Use Case 1: Table Generator
 Write a program that takes a number from the user and prints the multiplication table from 1 to 10 for that number.
Example:
 If user enters 5, output should be:
 5 x 1 = 5
 5 x 2 = 10
 ...
 5 x 10 = 50

num=int(input("Enter the number:"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)
