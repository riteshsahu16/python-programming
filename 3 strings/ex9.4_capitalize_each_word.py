# Q4. Write a program to accept a string and display string with capital letter of each word.
str1 = input()
for i in str1.split(' '):
    print(i.capitalize(), end=' ')