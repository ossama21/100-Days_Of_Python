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
choices = [rock, paper, scissors]
choice=int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)

if choice == 0 and computer_choice == 1:
    print(f"you chose: \n{rock}")
    print(f"computer chose: \n{paper}")
    print("you lose")
elif choice == 0 and computer_choice == 2:
    print(f"you chose: \n{rock}")
    print(f"computer chose: \n{scissors}")
    print("you win")
elif choice == 1 and computer_choice == 0:
    print(f"you chose: \n{paper}")
    print(f"computer chose: \n{rock}")
    print("you win")
elif choice == 1 and computer_choice == 2:
    print(f"you chose: \n{paper}")
    print(f"computer chose: \n{scissors}")
    print("you lose")
elif choice == 2 and computer_choice == 0:
    print(f"you chose: \n{scissors}")
    print(f"computer chose: \n{rock}")
    print("you lose")
elif choice == 2 and computer_choice == 1:
    print(f"you chose: \n{scissors}")
    print(f"computer chose: \n{paper}")
    print("you win")
elif choice == computer_choice:
    print(f"you chose: \n{choices[choice]}")
    print(f"computer chose: \n{choices[computer_choice]}")
    print("it's a tie")
else:
    print("invalid input")