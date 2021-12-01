print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0


if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print('Please Pay $5.')
        bill = 5
    elif age <= 18:
        print('Please Pay $7.')
        bill = 7
    elif age > 18:
        print('Please Pay $12.')
        bill = 12
    elif age >= 45 and age <= 55:
        bill = 0 
        print("Everything is going to be ok. Have a free ride on us!")
    wants_photos = input("Do you want a photo taken? Y or N. ")
    if wants_photos == 'Y':
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("You can't ride ")
