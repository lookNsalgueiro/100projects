import random

# random_integer = random.randint(1, 10)
# print(random_integer)

player_answer = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors"))
# 0, 1, 2

computer_answer = random.randint(0,2)
print(f"computer chose {computer_answer}")

if player_answer >= 3 or player_answer < 0:
    print("You typed an invalid number. Try again!")
elif player_answer == 0 and computer_answer == 2:
    print("You win!")
elif computer_answer == 0 and player_answer == 2:
    print("You lose!")
elif computer_answer > player_answer:
    print("You Lose!")
elif player_answer > computer_answer:
    print("You Win!")
elif computer_answer == player_answer:
    print("It's a draw!")


# ndom_float = random.uniform(1, 10)
# int(random_float)
