#Q6. Write a program to find the sum of the exponential series(accept values of x and n from user)
x = int(input())
n = int(input())
res = 1
for j in range(1, n+1):
    factorial = 1
    current = x**j
    for i in range(1, j+1):
        factorial *= i
    current /= factorial
    res += current
print(res)