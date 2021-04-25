# 16. Calculate bill
# Units Consumed          Charges
# 0-100                   0.50 per unit
# 101-200                 Rs. 50 plus Rs. 1 per unit over 100 units
# 201-300                 Rs. 150 plus 1.50 per unit over 200 units
# > 300                   Rs. 300 plus Rs.2 per unit over 300 units

unit = int(input())
amount = 0
if unit-100>0:
    unit -= 100
    amount += 100*0.5

    if unit-100>0:
        unit -= 100
        amount += 100*1

        if unit-100>0:
            unit -= 100
            amount += 100*1.5
        
        if unit>0:
            amount += unit*2

        else:
            amount += unit*1.5
    else:
        amount += unit *1
else:
    amount += unit *0.5

print(amount)
