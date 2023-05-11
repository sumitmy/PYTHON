# take user input
student_score = input("give the all student number and separate by space\n").split()

for n in range(0, len(student_score)):
    # str convert into integer
    student_score[n] = int(student_score[n])
print(f"all student score is {student_score}")

highest_score = 0

# compare with the every number given by user

for score in student_score:
    if score > highest_score:
        highest_score = score
print(f"the highest number is {highest_score}")
