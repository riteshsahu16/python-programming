# Q5. Write a program to accept a string and display the sum of the digits, if any present in string.
# numbers starts from 48 to 57
str1 = input()
sum_digits = 0
for i in str1:
    val = ord(i)
    if val >48 and val <=57:
        sum_digits += int(i)
print("sum of digits in string : ", sum_digits)