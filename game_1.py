from random import randint

def get_choice(choice):

    if choice == 'R':
        return 'Rock'
    elif choice == 'P':
        return 'Paper'
    elif choice == 'S':
        return 'Scissor'
    else:
        return 'Not a valid choice'


def main():

    print("Welcome to Rock, Paper, Scissor Game")
    print("[R]=Rock, [P]=Paper, [S]=Scissor, [Q]=Quit")

    counter = 1
    game_on = True
    choices = ["R", "P", "S"]

    while game_on:
        ### Input
        user_choice = input(f'Game {counter}, Please select your choice: ')
        user_choice = user_choice.upper()

        ## handle user input
        if user_choice == 'Q':
            print("Thank for joining, see you again")
            game_on = False
        else:
            ### compare user choice and computer choice:
            random_idx = randint(0, 2)
            computer_choice = choices[random_idx]
            
            print(f'You selected {get_choice(user_choice)} vs Computer choice is {get_choice(computer_choice)}')

            ### check result :

            if user_choice == 'R' and computer_choice == 'S':
                print("Congrats, you win. Rock beat Scissor")
            elif user_choice == 'P' and computer_choice == 'R':
                print("Congrats, you win. Paper covers Rock")
            elif user_choice == 'S' and computer_choice == 'P':
                print("Congrats, you win. Scissor cuts Paper")

            elif user_choice == 'S' and computer_choice == 'R':
                print('Sorry, computer wins. Rock beat Scissor')
            elif user_choice == 'P' and computer_choice == 'S':
                print("Sorry, computer wins. Scissor cuts Paper")
            elif user_choice == 'R' and computer_choice == 'P' :
                print("Sorry, computer wins. Paper covers Rock")
            elif user_choice == computer_choice:
                print(f"Wow It's a draw, Both you and Computer select {get_choice(user_choice)}")
            else:
                print("Invalid choice, please select [R], [P], [S], [Q] only")
            counter += 1
        print("==="*40)

if __name__ == '__main__':
    main()