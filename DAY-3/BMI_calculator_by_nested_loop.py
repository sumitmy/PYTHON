weight=input("body weight(kg): ")
height=input("height(m): ")
body_mass_index=int(weight)/float(height)**2
print("BMI is: ",body_mass_index)
if body_mass_index<18.5:
    print("underweight")
elif body_mass_index<25:
    print("normal weight")
elif body_mass_index<30:
    print("overweight")
elif body_mass_index<35:
    print("obese")
else:
    print("clinically obese")
