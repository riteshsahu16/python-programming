#Q4. Write a program to print first N odd no.
n = int(input())
count = 0
odd = 1
while count < n:
    print(odd, end=" ")
    count += 1
    odd += 2
