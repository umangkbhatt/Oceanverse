#Print a sequence of numbers starting from the number a with common difference d. Go on till you reach the number b.

#Enter a value for a: 10
#Enter a value for d: 3
#Enter a value for b: 20
#Output: 10 13 16 19

a = int(input("Enter a number of your choice: "))
d = int(input("Enter common difference of your choice: "))
b = int(input("Enter a Go-till number of your choice: "))

while a<=b:
    print(a)
    a = a+3
