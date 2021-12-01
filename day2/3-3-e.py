year = int(input("Which year do u want to check? "))

if year / 4 == 0:
    print('Leap year')
    if year / 100 == 0:
        print("Not leap year")
    else:
        print('leap year')
    if year / 400 == 0:
        print('leap year')
    else:
        print('not leap year')
else:
    print("Not Leap Year")

