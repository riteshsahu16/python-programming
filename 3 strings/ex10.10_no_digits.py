# Q10. Write a function in python which accept a string as argument and display total number of
# digits.
str1 = input()
count = 0
for i in str1:
    val = ord(i)
    if val >48 and val <=57:
        count += 1
print("no. of digits in string : ", count)