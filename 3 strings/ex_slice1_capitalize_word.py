# Q1. Accept a string from the user and display the string with first character of each word
# Capital. (Without using inbuilt function)
str1 = input()
for i in str1.split(' '):
    print(chr(ord(i[0])-32)+i[1:], end=" ")