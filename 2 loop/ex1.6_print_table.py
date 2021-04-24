#Q6. Write a program to print table of a number accepted from user.
n = int(input())
for i in range(1,11):
    print(n, "x", i, "=", n*i)
    #print(f"{n} x {i} = ", n*i)