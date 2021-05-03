# Q13. Write a program to display the unique words from the string.
str1 = input()
print("Unique Words : ")
c=0
for word in str1.split(' '):
    is_unique = True
    c = c+1
    for i in str1.split(' ')[c:]:
        if word == i:
            is_unique = False
            break
    if is_unique:
        print(word, end=' ')
    


