import random

options = {
    "R" : "Rock",
    "P" : "Paper",
    "S" : "Scissors"
}

opt = list(options.keys())


def main():
    player_choice = input(f"Chose a Letter from {opt} ")
    player_choice = player_choice.upper()
    computer_choice = random.choice(opt)


    def rule():
        if player_choice == 'R' and computer_choice == 'S':
            print("You win!")
        elif computer_choice == 'R' and player_choice == 'S':
            print("Computer Wins")
        elif player_choice == 'P' and computer_choice == 'R':
            print('You win')
        elif computer_choice == 'P' and player_choice == 'R':
            print("Computer Wins")
        elif player_choice == 'S' and computer_choice == 'P':
            print("You win")
        elif computer_choice == "S" and player_choice == "P":
            print("Computer Wins")

    if player_choice not in opt:
        print(f"You entered a wrong input {player_choice}")
        main()
    else:
        print(f"Player ({options[player_choice]}): CPU( {options[computer_choice]}) ")
        if player_choice == computer_choice:
            print("Its a tie!")
            main()
        else:
            rule()



main()