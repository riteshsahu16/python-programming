#Q8. Write a program to print numbers from a to b except multiple of 2 & 3.
a = int(input())
b = int(input())

for i in range(a, b+1):
    if i%2 !=0 and i%3 !=0:
        print(i, end=" ")