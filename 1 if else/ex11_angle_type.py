#[11] Whether the triangle will be an obtuse-angle, or a right-angle or an acute-angle triangle.
print("Enter three angles")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if(a+b+c != 180):
    print("invalid triangle")

elif(a>90 or b>90 or c>90):
    print("obtuse-angled triangle")
elif(a==90 and b<90 and c<90) or (b==90 and a<90 and c<90) or (c==90 and b<90 and a<90):
    print("right angled triangle")
else:
    print("acute-angled triangle")

