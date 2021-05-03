# Q3. Write a program to accept a string and display each word and it's length.

str1 = input()
for i in str1.split(' '):
    print(i, " length :", len(i))
