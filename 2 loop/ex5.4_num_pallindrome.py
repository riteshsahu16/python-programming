#Q4. Accept a number and check whether it is palindrome or not.
inp  = input()
count = 0 #to record no. of digits
for i in inp:
    count += 1
num = int(inp)
rev = ""
for i in range(count):
    last = num %10
    rev = rev + str(last)
    num = num//10
if rev == inp:
    print("Pallindrome")
else:
    print("NOT pallindrome")

