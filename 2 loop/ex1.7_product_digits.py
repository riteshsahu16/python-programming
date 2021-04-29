#Q7. Write a program to display product of the digits of a number accepted from the user.
n = int(input())
prod = 1
while n>0:
    last = n%10
    prod *= last
    n = n//10
print("product of digits : ", prod)
