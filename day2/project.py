# Day 2 final project
# Tip calc

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split_bill = int(input("How many people to split the bill? "))
total_bill_split = (total_bill / 100 * tip + total_bill) / split_bill
print(f"Each person should pay: ${round(total_bill_split, 2)}")
