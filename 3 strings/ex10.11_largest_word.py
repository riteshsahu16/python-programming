# Q11. Write a program to display the largest word from the string.
str1 = input()
max_length = 0
word = ''
for i in str1.split(' '):
    length = len(i)
    if length>max_length:
        word = i
        max_length = length

print("largest word is : ", word)