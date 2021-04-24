#Q5. Write a program to display all the numbers which are divisible by 11 but not by 2 between a and b.
a = int(input())
b = int(input())

for i in range(a, b+1):
    if i%11 == 0 and i%2 != 0:
        print(i, end=" ")
