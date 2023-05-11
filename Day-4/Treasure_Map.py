row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
matrix = [row1, row2, row3]
# print(matrix)

print(f"{row1}\n{row2}\n{row3}\n")
position = input("Where do you want to treasure: ")

horizontal = int(position[0])
vertical = int(position[1])

selected_row = matrix[vertical - 1]
print(selected_row )
selected_row[horizontal - 1] = "X"

# print(f"{row1}\n{row2}\n{row3}\n")
