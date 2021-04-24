#Q4. Write a program to display sum of odd numbers and even numbers that fall between a and b(including both numbers)  
a = int(input())
b = int(input())
sum =0
if (a%2==0):
    a += 1
for i in range(a, b+1, 2):
    print(i, end=" ")
    sum += i
print(" =", sum)