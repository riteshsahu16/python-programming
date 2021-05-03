# Q4. Write a program to accept string and display total number of alphabets.
# alphabets fall between 65-90 and 97-122
str1 = input()
no_alphabets = 0
for i in str1:
    val = ord(i)
    if (val>=65 and val<=90) or (val>=97 and val<=122):
        no_alphabets +=1
print("total no. of alphabets are: ", no_alphabets)
    
