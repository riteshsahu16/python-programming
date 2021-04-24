#Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.
#discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000
#orders of more than Rs. 100 for key-based toys, a discount of 5% is given
#discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500

print("enter product code:-> Battery-based : 1 \t Key-base : 2 \t Electric-based : 3 ")
code = int(input())
print("Enter order amount ")
amt = int(input())
net_price = amt
if(code==1 and amt>1000):
    net_price -= 0.1*amt
elif(code==2 and amt>100):
    net_price -= 0.05*amt
elif(code==3 and amt >500):
    net_price -= 0.1*amt
else:
    pass

print("Net Amount : ", net_price)