# Ordinary – 2500
# Pavillion – 3500
# Upper Pavillion – 4500
# Commentary Box – 6000
# VIP – 8000
# 10% discount for online booking    
# 8% discount for advance booking 
# no discount for  ticket window.
# Ask user to enter the booking type like online, advance or window booking.
# Ask user to select the types of seats.
# Compute the amount and print the ticket with proper format.

print("Enter code for MODE:\n O - Online Booking \n A - Advanced Booking \n W - Window Booking")
mode = input()
print("Enter Seat Type :\n O - Ordinary \n P - Pavillion \n U - Upper Pavillion \n C - Commentary Box \n V - VIP ")
seat_type = input()
amount = 0
discount = 0
if seat_type == "O":
    amount = 2500
elif seat_type == "P":
    amount = 3500
elif seat_type == "U":
    amount = 4500
elif seat_type == "C":
    amount = 6000
elif seat_type == "V":
    amount = 8000
       
if mode == "O":
        discount = amount * 0.1
elif mode == "A":
        discount = amount * 0.08

print("Cost for ", seat_type , " = ", amount )
print("Dicount in ", mode, " mode = ", discount)
amount -= discount
print("Grand Total : ", amount)

