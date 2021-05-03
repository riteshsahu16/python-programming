# Q8. Write a function in python which accept a string as argument and display total number of
# vowels.
str1 = input()
no_vowels= 0
for i in str1:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u': 
        no_vowels += 1
print("no of vowels : ", no_vowels)