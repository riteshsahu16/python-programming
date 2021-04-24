#Q3. Write a program to accept decimal number and display its binary number.
n = int(input())
tmp = ""
#divide n repeatedly by 2 till you get 1 as qoutient then take all the remainder in last to first order.
rem=n%2
quotient = n//2
n = n//2
count = 1
while True:
    tmp = tmp + str(rem)
    if quotient == 1:
        break
    rem = n%2
    quotient = n//2
    count +=1
    n = n//2
tmp = tmp + str(quotient)

# ans : Reverse(tmp)  : s[i] give i-th char of string s
print("Answer is : ")
for i in range(count, -1, -1):
    print(tmp[i], end="")

