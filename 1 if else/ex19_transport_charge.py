# Distance  Charges
# 1-50      8 Rs./Km
# 51-100    10 Rs./Km
#  >100      12 Rs/Km
# Ask user to enter the distance and compute the fare.

distance = int(input())
fare = 0
if distance<=50:
    fare = distance*8
elif distance >50 and distance<=100:
    fare = distance*10
else:
    fare = distance *12

print("fare : ", fare)