
import random
techniques = ['r', 'p', 's']


def vs_opponent():
    while True:
        com_choice = (random.choice(techniques))
        player_choice = input("r, p, or s? ")

        if com_choice == player_choice:
            print('Draw. Play again.')
            continue

        elif is_win(player_choice, com_choice):
            print('You Win!')
            break

        else:
            print('You lose!')
            break


def is_win(player, com):
    if (player == 'r' and com == 's') or (player == 's' and com == 'p') or (player == 'p' and com == 'r'):
        return True


vs_opponent()