# rock paper scissor game
import random

human_point = 0
computer_point = 0
chances = 5
no_of_chance = 0

print("You have only 10 chances")
print("Choose from\nrock\npaper\nscissor")

while no_of_chance < chances:
    inp = input("\nEnter your choice\n")
    options = ["rock", "paper", "scissor"]
    choice = random.choice(options)

    if inp == "rock" and choice == "paper":
        print(f"Your choice is {inp} and computer's choice is {choice}")
        computer_point = computer_point + 1
        print(f"You have {human_point} point and computer has {computer_point} point")

    elif inp == "paper" and choice == "paper":
        print(f"Your choice is {inp} and computer's choice is {choice}")
        print("This match has been drawn")
        print(f"You have {human_point} point and computer has {computer_point} point")

    elif inp == "scissor" and choice == "paper":
        print(f"Your choice is {inp} and computer's choice is {choice}")
        human_point = human_point + 1
        print(f"You have {human_point} point and computer has {computer_point} point")

    elif inp == "rock" and choice == "rock":
        print(f"Your choice is {inp} and computer's choice is {choice}")
        print("This match has been drawn")
        print(f"You have {human_point} point and computer has {computer_point} point")

    elif inp == "paper" and choice == "rock":
        print(f"Your choice is {inp} and computer's choice is {choice}")
        human_point = human_point + 1
        print(f"You have {human_point} point and computer has {computer_point} point")

    elif inp == "scissor" and choice == "rock":
        print(f"Your choice is {inp} and computer's choice is {choice}")
        computer_point = computer_point + 1
        print(f"You have {human_point} point and computer has {computer_point} point")

    elif inp == "rock" and choice == "scissor":
        print(f"Your choice is {inp} and computer's choice is {choice}")
        human_point = human_point + 1
        print(f"You have {human_point} point and computer has {computer_point} point")

    elif inp == "paper" and choice == "scissor":
        print(f"Your choice is {inp} and computer's choice is {choice}")
        computer_point = computer_point + 1
        print(f"You have {human_point} point and computer has {computer_point} point")

    elif inp == "scissor" and choice == "scissor":
        print(f"Your choice is {inp} and computer's choice is {choice}")
        print("This match has been drawn")
        print(f"You have {human_point} point and computer has {computer_point} point")

    else:
        print("You have input wrong value")

    no_of_chance = no_of_chance + 1
    print(f"{chances - no_of_chance} chances left out of {chances}")

print("Game over")

if computer_point > human_point:
    print("Computer wins and you loose\nTry again next time")

if computer_point < human_point:
    print("Congrats you win and computer loose")

if computer_point == human_point:
    print("This is a tie between both of you")
a = input()

