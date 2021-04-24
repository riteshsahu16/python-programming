#[8] Find maximum number out of given three numbers.
print("Enter three no.")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if(a==b and b==c):
    print("all are equal")

elif (a==b and a>c) or (a==c and a>b) or (a>b and a>c):
    if(a==b):
        print("a and b are equal & greatest")
    elif(a==c):
        print("a and c are equal & greatest")
    else:
        print("a is greatest")
elif (b==c and b>a) or (b>a and b>c):
    if(b==c):
        print("b and c are equal & greatest")
    else:
        print("b is greatest")
else:
    print("c is greatest")