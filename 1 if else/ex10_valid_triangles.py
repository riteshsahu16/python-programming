#[10] Write a program that reads three positive numbers a, b, c and determines whether they can form the three sides of a triangle.
print("Enter three sides")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if(a+b>c or a+c>b):
    print("valid triangle")
else:
    print("Not valid triangles")