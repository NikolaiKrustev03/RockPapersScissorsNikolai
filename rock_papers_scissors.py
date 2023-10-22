import random
ai_input=["rock","papers","scissors"]
pc_won="Computer won\n"
p_won="Player won\n"
def game():
    while True:
        try:
            player_input=input("rock, papers, scissors?\n").lower()
            if player_input in ai_input:
                break
            else:
                raise Exception("Invalid input, please input rock, papers or scissors only")
        except Exception as err:
            print(err)
    ai_move=random.choice(ai_input)
    print(f"Computer chose: {ai_move}")
    print(f"Player chose: {player_input}")
    if player_input==ai_move:
        print("It's a tie\n")
    elif player_input=="rock":
        if ai_move=="scissors":
            print(p_won)
        else:
            print(pc_won)
    elif player_input=="papers":
        if ai_move=="rock":
            print(p_won)
        else:
            print(pc_won)
    else:
        if ai_move=="rock":
            print(pc_won)
        else:
            print(p_won)

game()

while True:

    try:
        continue_game = input("Would you like to continue? (Y/N)\n")
        if continue_game=="Y":
            guess_num()
        elif continue_game=="N":
            print("Maybe you'd like to check out my other projects on https://github.com/NikolaiKrustev03")
            break
        elif not continue_game.isalpha():
            print(f"{continue_game} not allowed. Only Y or N as a valid answer")
        else:
            print("Only Y or N as a valid answer")

    except ValueError:
        print("Invalid answer")
