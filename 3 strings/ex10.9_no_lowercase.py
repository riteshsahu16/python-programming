# Q9. Write a function in python which accept a string as argument and display total number of
# lower case characters.
str1 = input()
lower  = 0
for i in str1:
    val = ord(i)
    if val>=97 and val<=122:
        lower +=1
print("lowercase : ", lower)