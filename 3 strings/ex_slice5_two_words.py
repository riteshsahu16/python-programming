# Q5. Accept a String from the user and display first two characters of each word in same
# line separated by space.
str1 = input()
for i in str1.split(' '):
    print(i[:2], end=' ')