import random
person_name=input("give me all person name and seperate by comma:\n")
name=person_name.split(",")
print(name)
person_pay_bill=random.choice(name)
print(person_pay_bill+" is paying the bill")
