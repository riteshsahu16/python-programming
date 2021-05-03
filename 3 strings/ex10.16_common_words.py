# Q16. Write a program to accept two strings from the user and display the common words.(Ignore
# case)
str1 = input()
str2 = input()
print("COmmon WOrds : ")
for i in str1.split(' '):
    for j in str2.split(' '):
        if i.lower() == j.lower():
            print(i, end=' ')