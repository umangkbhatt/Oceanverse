# Write a program that takes a number n from the user and prints the multiplication table for that number from 1 to 10. Generalize it from i  to j.

# 2X1=2
# 2X2=4
# and so on...

# Hard coding for values 1 to 10

# We take the input from User
"""n = int(input("Enter a number n for the multiplication table: "))

# Loop iterates i for the fix range of 1 to 11 (Remember, here 11 is not included)
for i in range(1,11):
    print(n, "*", i, "=", n * i)
"""
# Generalizing it from i to j

# We take the input from User
n = int(input("Enter a number n for the multiplication table: "))

# Here, we take two other inputs which demarks start and end of the iteration in for-loop
i = int(input("Enter start value: "))
j = int(input("Enter end value: "))

# Loop iterates i for the flexiable values i and j+1 
for k in range(i, j+1):
    print(n, "*", k, "=", n * k)