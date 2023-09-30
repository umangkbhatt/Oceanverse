#Write a program that takes a number n from the user and prints the multiplication table for that number from 1 to 10. Generalize it from i  to j.

#2X1=2
#2X2=4
#and so on...

#hard coding for values 1 to 10

"""n = int(input("Enter a number n for the multiplication table: "))

for i in range(1,11):
    print(n, "*", i, "=", n * i)
"""
#Generalizing it from i to j

n = int(input("Enter a number n for the multiplication table: "))

i = int(input("Enter start value: "))
j = int(input("Enter end value: "))

for k in range(i, j+1):
    print(n, "*", k, "=", n * k)