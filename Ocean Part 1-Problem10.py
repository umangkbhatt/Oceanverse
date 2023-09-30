#Write a program to find out if the given number is prime or not (1 point).

n = int(input("Enter natural number: "))

i = 1;

#As of now I know only brute force technique which is to figure out more than 2 factors. 

count = 0

while i<=n:
    if n%2 == 0:
        print(n , " It is not prime")
        break
    elif(n%i==0):
        count= count + 1
        if (count>2):
            print(n , " It is not prime")
            break
    i = i+1
if(count==2):
    print(n, " is prime number")
    

