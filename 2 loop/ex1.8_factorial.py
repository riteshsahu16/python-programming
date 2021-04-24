#Q8. Write a program to find the factorial of a number.
n = int(input())
factorial = 1
while n>0:
    factorial *= n
    n -= 1
print(factorial)