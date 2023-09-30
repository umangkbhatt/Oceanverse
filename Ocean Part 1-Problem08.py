#Write a program that calculates and prints the sum of all numbers from 1 to n, where n is provided by the user (1 point).

# The variable 'sum' will add up all the values from 1 to n (Here, n is included)
sum = 0 
# We take the input from User
n = int(input("Enter number: "))
# Loop will iterate i for the range until n+1
for i in range(n+1):
    sum = sum + i
print(sum)
