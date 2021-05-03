# Q18. Write a program to display the smallest word from the string.
str1 = input()
min_length = len(str1.split(' ')[0])
word = str1.split(' ')[0]
for i in str1.split(' ')[1:]:
    length = len(i)
    if length<min_length:
        word = i
        min_length = length

print("smallest word is : ", word)