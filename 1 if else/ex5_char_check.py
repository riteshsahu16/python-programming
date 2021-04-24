#[5] The given character is an uppercase letter or lowercase letter or a digit or a special character.
ch = ord(input())
if ch>=33 and ch<=47:
    print("special character")
elif ch>=48 and ch<=57:
    print("number")
elif ch>=65 and ch<=90:
    print("Upper case alphabet")
elif ch>=97 and ch<=122:
    print("Lower case alphabet")
else:
    print("other character")