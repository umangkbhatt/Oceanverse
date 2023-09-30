# Write a program to take as input a number n  and display the first n natural numbers 

n = int(input("Enter natural number of your choice: "))

# Loop iterates i for the range 1 to n+1. Remember, we want 'n' to be included for iteration. There, we take 'n+1'.
for i in range(1,n+1):
    print(i)