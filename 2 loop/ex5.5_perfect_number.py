#Q5. Write a program to accept a number and check whether it is a perfect number or not.
n = int(input())
i = 1
sum_factor = 0
while(i<= n/2):
    if n%i ==0:
        sum_factor += i
    i += 1

print("sum : ",sum_factor)
if sum_factor == n:
    print("Perfect Num")
else:
    print("NOT Perfect Num")
