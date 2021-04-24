count = 0
avg = 0
n = int(input())
while n != 0:
    avg += n
    n = int(input())
    count += 1
avg /= count
print(avg)