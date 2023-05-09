print("welcome to pizza delivery")
size=input("size of pizza 's' for small, 'm' for medium ,'l' for large\n")
if size=="s":
    bill=100
    print("small pizza price is:",bill)
elif size=="m":
    bill=150
    print("medium pizza price is:",bill)
else:
    bill=200
    print("large pizza price is:",bill)
pepperoni=input("pepperoni for small type's' or large typr 'l'\n")
if pepperoni=="s":
    bill+=20
    print("pepperoni with small pizza bill is:",bill)
else:
    bill+=50
    print("pepperoni with large pizza bill is:",bill)
extra_cheese=input("if you want extra cheese then type 'y' or not 'n'\n ")
if extra_cheese=="y":
    bill+=50
    print("your final bill is:",bill)
else:
    print("your final bill is:",bill)
