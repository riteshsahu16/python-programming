# Category          Units                               Rate
# Commercial        Minimum up to 5000 units            Rs. 1500
#                   Next 5000 units                     Rs. 0.25 per unit
#                   Next 10000 units                    Rs. 0.23 per unit
#                   Above this                          Rs. 0.20 per unit
# Institutional
#                   Minimum up to 5000 units            Rs. 1800
#                   Next 5000 units                     Rs. 0.30 per unit
#                   Next 10000 units                    Rs. 0.28 per unit
#                   Above this                          Rs. 0.25 per unit
# Domestic
#                   Minimum up to 100 Units             Rs. 75
#                   Next 100 Units                      Rs. 1.25 per unit
#                   Next 200 Units                      Rs. 2.00 per unit
#                   Above this                          Rs. 2.50 per unit

# Ask user to enter customer category, Units.
# Compute the bill as per given criteria.
# Print bill in proper format.

print("Enter a category acc to CODE :\n Commercial : C \n Institutional : I \n Domestic : D")
category = input()
print("Enter the amount of UNITS consumed : ")
units = int(input())
bill = current = 0
print("Bill Costing: ", end=" ")
if category == "C":
    current = 1500
    bill += current
    print(current, end=" ")
    units -= 5000
    if units-5000>0:
        current = 5000 * 0.25
        bill += current
        print(" + ",current, end=" ")
        units -= 5000
        if units-10000>0:
            current = 10000*0.23
            bill += current
            print(" + ",current, end=" ")
            units -= 10000
            if units>0:
                current = units*0.20
                bill += current
                print(" + ",current, end=" ")
        else:
            current = units*0.23
            bill += current
            print(" + ",current, end=" ")
    else:
        current = units * 0.25
        bill += current 
        print(" + ",current, end=" ")
        
elif category == "I":
    current = 1800
    bill += current
    print(current, end=" ")
    units -= 5000
    if units-5000>0:
        current = 5000 * 0.30
        bill += current
        print(" + ",current, end=" ")
        units -= 5000
        if units-10000>0:
            current = 10000*0.28
            bill += current
            print(" + ",current, end=" ")
            units -= 10000
            if units>0:
                current = units*0.25
                bill += current
                print(" + ",current, end=" ")
        else:
            current = units*0.28
            bill += current
            print(" + ",current, end=" ")
    else:
        current = units * 0.30
        bill += current 
        print(" + ",current, end=" ")

elif category == "D":
    current = 75
    bill += current
    print(current, end=" ")
    units -= 5000
    if units-5000>0:
        current = 5000 * 1.25
        bill += current
        print(" + ",current, end=" ")
        units -= 5000
        if units-10000>0:
            current = 10000*2.0
            bill += current
            print(" + ",current, end=" ")
            units -= 10000
            if units>0:
                current = units*2.5
                bill += current
                print(" + ",current, end=" ")
        else:
            current = units*2.0
            bill += current
            print(" + ",current, end=" ")
    else:
        current = units *2.5
        bill += current 
        print(" + ",current, end=" ")


print("\n Grand Total =", bill)