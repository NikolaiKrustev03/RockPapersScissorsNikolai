import random
ai_input=["rock","papers","scissors"]
pc_won="Computer won"
p_won="Player won"
while True:
    try:
        player_input=input("rock, papers, scissors?")
        if player_input==ai_input[0] or player_input==ai_input[1] or player_input==ai_input[2]:
            break
        else:
            raise Exception("Invalid input, please input rock, papers or scissors only")
    except Exception as err:
        print(err)
ai_move=random.choice(ai_input)
print(f"Computer chose {ai_move}")
print(f"Player chose {player_input}")
if player_input==ai_move:
    print("It's a tie")
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