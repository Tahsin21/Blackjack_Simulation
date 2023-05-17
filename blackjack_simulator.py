cards = [2,3,4,5,6,7,8,9,10,10,10,10,0] #use 0 as a case for either 1 or 11
p1,p2 = 0
p1_win, p2_win = 0
gameCount = 0
hit = True

def basicStrat(player, dealer):
    if (player == 13 or 14 or 15 or 16 or 17) and (dealer == 2 or 3 or 4 or 5 or 6):
        hit = False
    elif (player == 12) and (dealer == 4 or 5 or 6):
        




