ch = ord(input())
i = 65
j =  count = 1
while chr(i) != chr(ch+1):
    t = 1
    while(i<=ch and t<=count ):
        print(chr(i), end=" ")
        i += 1
        t+=1
    count += 1
    print()
