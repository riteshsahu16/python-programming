
amount = int(input())
net_amt = amount
code = input()
if code == "sh":
    if amount >100 and amount <=200:
        amount -= 0.05 *amount
    elif amount>200 and amount <=300:
        amount -= 0.1 *amount
    else:
        amount -= 0.18 *amount
elif code == "p":
    if amount<=100:
        amount -= 0.03 *amount
    elif amount >100 and amount <=200:
        amount -= 0.08 *amount
    elif amount >200 and amount <=300:
        amount -= 0.12 *amount
    else:
        amount -= 0.2 *amount
elif code == "sht":
    if amount<=100:
        amount -= 0.05 *amount
    elif amount >100 and amount <=200:
        amount -= 0.1 *amount
    elif amount >200 and amount <=300:
        amount -= 0.15 *amount
    else:
        amount -= 0.22 *amount
print("bill : ", amount)
print("discount : ", net_amt-amount)