# [3] The given number is of one digited or two digited or three digited or more than three digited. 
n = int(input())
count = 0
quotient = n//10
if(quotient>100):
    print("More than 3 digits")
elif(quotient>10 and quotient<100):
    print("3 digit no.")
elif(quotient>0 and quotient<10):
    print("2 digit no.")
else:
    print("1 digit no.")


#short hand if-else
print("3d+") if(quotient>100) else print("3d") if(quotient>10 and quotient<100) else print("2d") if(quotient>0 and quotient<10) else print("1d")




