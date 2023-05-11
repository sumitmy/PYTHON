# take user input
#  10 20 30 40
# student_score are in string format
student_score = input("give the all student number and separate by space\n").split()
# ['10','20','30','40']

# to covert substring into integer and append into new list
# new_student is in integer format
new_student = []

# print height in the list form
for student in student_score:
    x = int(student)
    new_student.append(x)

print(f"all student score is {new_student}")

highest_score = 0

# compare with the every number given by user

for score in new_student:
    if score > highest_score:
        highest_score = score
print(f"the highest number is : {highest_score}")
