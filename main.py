import game,utils



def play_game():
    Win=None
    playrs={'playr_1':0,'playr_2':0}
    passe=False
    while True:
        for playr,i in playrs.items():
            print(playr,i)
            a=utils.turn_decision()
            if a =="r":
                playrs[playr]+=game.roll_two_d6()
                print(playr,playrs[playr])
                passe=False
            else:
                if passe:
                    Win=max(playrs.items())
                else:
                    passe=True








a=play_game()




