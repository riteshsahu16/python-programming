#Q3. Write a program to print all prime numbers that fall between two numbers including both
a = int(input())
b = int(input())

for i in range(a, b+1):
    j =2
    is_prime = True
    while(j <= i//2):
        if i%j==0:
            is_prime = False
            break
        j += 1
    if is_prime:
        print(i, end=" ")
    