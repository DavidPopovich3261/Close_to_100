import random


def roll_two_d6() -> int:
    dice_a=random.randint(1,6)
    dice_b=random.randint(1,6)
    dice=int(dice_a+dice_b)
    return dice




def tie_breaker(players):
    while 'player_a'== 'player_b':
        players['player_a']=roll_two_d6()
        players['player_b'] = roll_two_d6()
    if 'player_a'>'player_b':
        return "player_a"
    return "player_b"



