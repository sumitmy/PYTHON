import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images = [rock, paper, scissors]
flag = True
while flag:
    # take user choice
    print("welcome to the rock paper and scissors game")
    user_choice = int(input("for Rock type '0', paper '1', scissors '2' or -1 to stop the game :\n"))
    if user_choice >= 3 :
        print("invalid number...")
        break
    if user_choice == -1:
        print("Bye Bye")
        break
    print("user choice")
    print(images[user_choice])

    # for computer random choice
    computer_choose = random.randint(0, 2)
    print(f"computer choice is: {computer_choose}")
    print(images[computer_choose])

    # paper win against Rock
    if user_choice == 1 and computer_choose == 0:
        print("you win")
    # rock win against scissor
    elif user_choice == 0 and computer_choose == 2:
        print("you win")
    # Scissor win against paper
    elif user_choice == 2 and computer_choose == 1:
        print("you win")
    # if both are equal then game is draw
    elif user_choice == computer_choose:
        print("match draw")

    # following above all condition are false then you lose the game
    else:
        print("you lose")
        print("Better luck next time")
