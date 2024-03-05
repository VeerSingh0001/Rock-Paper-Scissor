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


again = "yes"
while again == "yes":  
    userInpute = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ")
    cmptrChos  = random.randint(0,2)
    options = [rock, paper, scissors]
    validInputes = ["0","1","2"]
    while userInpute not in validInputes :
        print("Please type correct number!") 
        userInpute = (input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))


    userInpute = int(userInpute)
    print(f"{options[userInpute]}")
    print("Computer chose")
    print(f"{options[cmptrChos]}")

    if userInpute == cmptrChos:
        print("Match Draw!")
    elif userInpute == 0 and cmptrChos == 1 or userInpute == 2 and cmptrChos == 0 or userInpute == 1 and cmptrChos == 2:
        print("You lose!")
    elif userInpute == 1 and cmptrChos == 2 or userInpute == 1 and cmptrChos == 0 or userInpute == 2 and cmptrChos == 1:
        print("You won!")
        pass
    ask = input("Wanna play again? ").lower()
    again = ask
print("Thanks for playing!")