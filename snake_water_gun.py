# SNAKE WATER GUN
# TAKE 2 INPUT 1 RANDOM FROM PC ANOTHER FROM USER
import random

print("SNAKE WATER GUN game\n\t s FOR SNAKE \n\t w FOR WATER\n\t g FOR GUN")
rounds = 5
winner = "No one"
computer_points = 0
user_points = 0
user__input = "SNAKE"
while rounds > 0:
    computer_count = [1, 2, 3]
    choice = random.choice(computer_count)
    user_input = input("enter your choice :")
    user_count = 0
    print(choice)
    computer_input = "SNAKE"
    if choice == 1:
        computer_input = "SNAKE"
    elif choice == 2:
        computer_input = "WATER"
    elif choice == 3:
        computer_input = "GUN"
    if user_input == "s":
        user_count = 1
        user__input = "SNAKE"
    elif user_input == "w":
        user_count = 2
        user__input = "WATER"
    elif user_input == "g":
        user_count = 3
        user__input = "GUN"
    if (user_count == 3 and choice == 1) or (user_count == 2 and choice == 3) or(user_count == 1 and choice == 2):
        user_points = user_points + 1
    elif (user_count == 3 and choice == 2) or (user_count == 2 and choice == 1) or(user_count == 1 and choice == 3):
        computer_points = computer_points + 1
    print("user_choice", user__input, "computer choice", computer_input)
    rounds = rounds - 1
    print("rounds remaining", {rounds}, "your points", {user_points}, "computer points", {computer_points})
    if user_points > computer_points:
        winner = "You"
    elif user_points < computer_points:
        winner = "Computer"
    elif user_points == computer_points:
        winner = "No one"
print("round over winner is ", winner)
