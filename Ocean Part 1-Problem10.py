# Write a program to find out if the given number is prime or not (1 point).
n = int(input("Enter natural number: "))

# Variable which act as denominator 
i = 1;

# As of now I know only brute force technique which is to figure out more than 2 factors. 

# Variable keeps the track of factors
count = 0

# Loop will be false, if count is greater than 2
while i<=n:
    # Condition checks for 1 being special case
    if n==1: 
        print("Number 1 is not prime")
    # Condition checks if input number is even
    if n%2 == 0: 
        print(n , " It is not prime")
        break
    # Condition iterates and divide input with incremental values of i
    elif(n%i==0):
        # The count variable keeps track of factors  
        count= count + 1
        # Condition checks, if count is greater than two factors 
        if (count>2): 
            print(n , " It is not prime")
            break
    i = i+1
# Finally, it checks if count is exactly 2 then we can conclude the number to be prime number
if(count==2):
    print(n, " is prime number")
    

