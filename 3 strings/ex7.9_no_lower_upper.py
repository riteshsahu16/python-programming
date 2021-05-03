# Q9. Write a program to count the number of lowercase and uppercase character in a
# string accepted from the user.
str1 = input()
lower = upper = 0
for i in str1:
    val = ord(i)
    if val>=65 and val<=90:
        upper += 1
    elif val>=97 and val<=122:
        lower +=1
print("lowercase : ", lower, " upper : ", upper)