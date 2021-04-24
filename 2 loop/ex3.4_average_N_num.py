#Q2. Accept N numbers from the user and display their average.
n = int(input())
avg = 0
t = n
while(t>0):
    num = int(input())
    avg += num
    t -= 1
avg /= n
print(avg)
