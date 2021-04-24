#Read any two positive integer numbers (say n1 & n2) and one character type operator (say opr). Note that opr is any mathematical operator.

n1 = int(input("n1 : "))
n2 = int(input("n2 : "))

opr = input("enter operator : + - * / : ")
res = 0
if opr == '+':
    res = n1 + n2
elif opr == '-':
    res = n1 - n2
elif opr == '*':
    res = n1 * n2
elif opr == '/':
    res = n1 / n2
else:
    print("unkown operation")

print("result : ", res)