number = input("enter a number: ")
result = 0
for i in number:
    print("Single digit: " + i)
for i in number:
    result += int(i)
print("sum of all digits of a number ", result)
