name_1 = input("first name is: ")
name_2 = input("second name is: ")
combination_name = name_1 + name_2
new_name = combination_name.lower()
t = (new_name.count('t'))
r = (new_name.count('r'))
u = (new_name.count('u'))
e = (new_name.count('e'))
true = t + r + u + e
l = (new_name.count('l'))
o = (new_name.count('o'))
v = (new_name.count('v'))
e = (new_name.count('e'))
love = l + o + v + e
love_score = str(true) + str(love)

print(f"your love percentage is {love_score}")
