#Take year as year from the user
year=int(input("Enter year: "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Not a Leap year",year)
        else:
            print("Not a leap year: ",)
    else:
        print("Leap year: ",year)
else:
    print("Not a Leap year: ",year)