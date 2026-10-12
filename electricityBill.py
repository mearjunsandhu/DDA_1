# Electricity Bill Calculator
# Write a program that calculates the electricity bill based on units consumed using different rates for different slabs.

# 100 and below = 3
# 100-200 = 5
# 200-300 = 7
# 300 above = 10


# Taking Units Consumed as Input
units = int(input("Enter Units Consumed: "))

# Calculating Bill Based on Slabs
if units <= 100:
    totalBill = units * 3
elif units <= 200:
    totalBill = units * 5
elif units <= 300:
    totalBill = units * 7
else:
    totalBill = units * 10

# Displaying the Final Bill
print(f"Total Electricity Bill: {totalBill}")