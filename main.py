from random import choice
from time import sleep

d_items = {'ROCK': 1, 'SCISSORS': 2, 'PAPER': 3}
score = {'Player': 0, 'Computer': 0}


def take_and_translate():
    while True:
        text = input("""
Enter your move (rock, scissors, paper, or r, s, p) to move,
type 'exit' to quit, type 'new' to start new game
""")
        if text.upper() in ('ROCK', 'R'):
            text = 'ROCK'
        elif text.upper() in ('SCISSORS', 'S'):
            text = 'SCISSORS'
        elif text.upper() in ('PAPER', 'P'):
            text = 'PAPER'
        elif text.upper() == 'EXIT':
            print('GOODBYE!')
            sleep(1.5)
            quit()
        elif text.upper() == 'NEW':
            global score
            score = {'Player': 0, 'Computer': 0}
            print('Starting new game')
            continue
        else:
            print('Try again')
            continue
        return text


def play(player_move):
    for i in range(3, 0, -1):
        print(i)
        sleep(0.3)
    pc_move = choice(list(d_items.keys()))
    print(player_move, 'vs', pc_move)
    if d_items[player_move] == d_items[pc_move]:
        print("It's a draw!")
    elif d_items[player_move] - d_items[pc_move] in (-1, 2):
        print('You won!!!')
        score['Player'] += 1
    else:
        print('You lost!')
        score['Computer'] += 1
    print(f"YOU {score['Player']} : {score['Computer']} COMPUTER")


while True:
    move = take_and_translate()
    play(move)
