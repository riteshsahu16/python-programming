#Q10. Write a program to check whether a number is prime or not.
n = int(input())
i = 2
is_prime = True
while(i <= n**0.5):
    if n%i==0:
        is_prime = False
        break
    i += 1
if is_prime:
    print("The no. is prime")
else:
    print("The no. is NOT prime")
