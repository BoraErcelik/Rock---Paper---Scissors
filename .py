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

me = int(
  input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
computer = random.randint(0, 2)
if me == 0:
  print(rock)
  if computer == 0:
    print(rock)
    print("It's draw!")
  elif computer == 1:
    print(paper)
    print("You lose!")
  elif computer == 2:
    print(scissors)
    print("You win!")
  else:
    print("Fail!! You need to choose a number between 0 and 2")
elif me == 1:
  print(paper)
  if computer == 0:
    print(rock)
    print("You win!")
  elif computer == 1:
    print(paper)
    print("It's draw!")
  elif computer == 2:
    print(scissors)
    print("You lose!")
  else:
    print("Fail!! You need to choose a number between 0 and 2")
elif me == 2:
  print(scissors)
  if computer == 0:
    print(rock)
    print("You lose!")
  elif computer == 1:
    print(paper)
    print("You win!")
  elif computer == 2:
    print(scissors)
    print("It's draw!")
  else:
    print("Fail!! You need to choose a number between 0 and 2")
else:
  print("Fail!! You need to choose a number between 0 and 2")
