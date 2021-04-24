#Q8. Write a program to find the sum of GP series, taking a, r, n as input
# a + ar + ar2 + ar3 + ………..arn
a = int(input())
r = int(input())
n = int(input())
res = a
for i in range(1, n+1):
    res += a * r**i
print(res)