# Q1. Accept a string and display in reverse order.
#using slicing
str1 = input()
print(str1[::-1])

#Alternatively using range
reverse = ''
for i in range(len(str1)-1, -1, -1):
    reverse = reverse + str1[i]
print(reverse)