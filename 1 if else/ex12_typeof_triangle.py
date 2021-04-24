#[12] If the triangle is an acute angle triangle, determine further whether the triangle is equilateral, isosceles, or scalene.
print("Enter three sides")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if !(a+b>c or a+c>b):
    print("Invalid triangle")
elif(a==b and a==c):
    print("equilateral triangle")
elif(a=b or a=c or b=c):
    print("Isoceles triangle")
else:
    print("scalene triangle")