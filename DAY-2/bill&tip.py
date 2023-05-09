print("Welcome to the tip calculator!")
bill=float(input("What was the total bill? "))
tip=int(input("How much tip would you like to give? 10, 12 ,13 or 15 "))
people=int(input("how many people to split to bill?"))
tip_percent=tip/100
tip_amount=tip*tip_percent
total_bill=bill+tip_amount
bill_per_person=total_bill/people
final=round(bill_per_person,2)
print("Each person should pay: ",final)