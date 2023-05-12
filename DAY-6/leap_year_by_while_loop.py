# take input in integer fromat
year = int(input("Enter a year: "))

is_leap_year = False

# start while loop to check year is leap year or not
while True:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                is_leap_year = True
            else:
                is_leap_year = False
        else:
            is_leap_year = True
    else:
        is_leap_year = False

    if is_leap_year:
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")

    # if user wnat to check some other is year type 'y' or not then type 'n'
    repeat = input("Do you want to check another year? (y/n): ")

    # if user type 'n' then condition break
    if repeat.lower() == "n":
        print("bye bye!")
        break

    # again take input  bye user
    year = int(input("Enter a year: "))
