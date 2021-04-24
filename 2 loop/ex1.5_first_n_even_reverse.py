#Q3. Write a program to print first N even no. in reverse order
n = int(input())
# n = 10
# even = 0 : 9*2 = 18

even = (n-1) * 2
while even >= 0:
    print(even, end=" ")
    even -= 2