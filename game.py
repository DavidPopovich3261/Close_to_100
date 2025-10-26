import random


def roll_two_d6() -> int:
    dice_a=random.randint(1,6)
    dice_b=random.randint(1,6)
    dice=int(dice_a+dice_b)
    return dice




def tie_breaker(*roller):
    player_a,player_b=0,0
    while player_a== player_b:
        player_a=roll_two_d6()
        player_b=roll_two_d6()
    if player_a>player_b:
        return "player_a"
    return "player_b"



