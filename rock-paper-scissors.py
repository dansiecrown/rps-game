import random

options = ["R","P","S"]



def main():
    player_choice = input(f"Chose a Letter from {options} ")
    player_choice = player_choice.upper()
    computer_choice = random.choice(options)
    print("I got here")

    def rule():
        if player_choice == 'R' and computer_choice == 'S':
            print("You win!")
        elif computer_choice == 'R' and player_choice == 'S':
            print("You lose")
        elif player_choice == 'P' and computer_choice == 'R':
            print('You win')
        elif computer_choice == 'P' and player_choice == 'R':
            print("You lose")
        elif player_choice == 'S' and computer_choice == 'P':
            print("You win")
        elif computer_choice == "S" and player_choice == "P":
            print("You lose")

    if player_choice not in options:
        print(f"You entered a wrong input {player_choice}")
        main()
    else:
        if player_choice == computer_choice:
            print("Its a tie!")
            main()
        else:
            print(player_choice, computer_choice)
            rule()



main()