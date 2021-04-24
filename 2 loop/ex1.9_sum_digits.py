#Q9. Write a program to find the sum of the digits of a number accepted from user
n = int(input())
sum = 1
while n//10>0:
    last = n%10
    sum += last
    n = n//10
print("product of digits : ", sum)