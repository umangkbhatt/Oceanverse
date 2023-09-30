#Write a program that calculates and prints the sum of all numbers from 1 to n, where n is provided by the user (1 point).

sum = 0 
n = int(input("Enter number: "))
for i in range(n+1):
    sum = sum + i
print(sum)
