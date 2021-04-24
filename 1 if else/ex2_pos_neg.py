#[2] The given number is positive or negative or zero. 
n = int(input())

if(n>0):
    print("positive")
elif(n<0):
    print("negative")
else:
    print("zero")


#if-else shorthand
print("pos") if(n>0) else print("neg") if(n<0) else print("zero")

