#welcome in Car Racing
height=int(input("what is your hright in cm: "))
if height>=120:
    print("you are eligible for drive car")
    age=int(input("what is your age: "))
    if age<12:
        bill=100
        print("you are a chlid and your ticket is: ",bill)
    elif age<=18:
        bill=150
        print("you are young and your ticket is: ",bill)
    else:
        bill=200
        print("you are adult and your ticket is: ",bill)
    take_photo=input("take photo or not press Y for yes & N for no?")
    if take_photo=="y":
        bill+=30
        print("final bill is: ",bill)
    else:
        print("final bill is: ",bill)
else:
    print("you are not eligible for drive car")