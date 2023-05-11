# take user height as input and seperate by the space
users_height = input("give users heights of different persons seperated by spaces\n").split()

# print height in the list form
for n in range(0, len(users_height)):
    users_height[n] = int(users_height[n])

print("user height is:", users_height)
total_height = 0
# start for loop,for count the sum of all users height
for height in users_height:
    total_height += height

print("total height is:", total_height)
users_number = 0

# count number of user
for users in users_height:
    users_number += 1

print("total number of user is:", users_number)
# count average by dividing sum of total height to user number
average_height = round(total_height / users_number)
print("average of all users height is:", average_height)
