import sys

def red_blue_nim(num_r, num_b, player1, d):
    
    def next(st):                                 #Points to the successor function
        red = []
        blue = []
        if st[0] < st[1]:
            red = [(st[0] - 1, st[1])] if st[0] > 0 else []
        else:
            blue = [(st[0], st[1] - 1)] if st[1] > 0 else []
        return red + blue
    
    def term_st(st):                                    #Checks if the terminal state is reached
        return st[0] == 0 or st[1] == 0
    
    def getnextmove(st, d):                             #Calculates next move
        max = float('-inf')
        best = None
        for s in next(st):
            v = minmax_ab(s, d - 1, float('-inf'), float('inf'), False)
            if v > max:
                max = v
                best = s
        return best
    
    def minmax_ab(st, d, a, b, ismax):         #Min Max Alpha Beta Pruning with Depth
        if d == 0 or term_st(st):
            return util(st)

        if ismax:
            v = float('-inf')
            for s in next(st):
                v = max(v, minmax_ab(s, d - 1, a, b, False))
                a = max(a, v)
                if b <= a:
                    break
            return v
        else:
            v = float('inf')
            for s in next(st):
                v = min(v, minmax_ab(s, d - 1, a, b, True))
                b = min(b, v)
                if b <= a:
                    break
            return v
        
    def util(st):                                    #Calculates the utility value
        return 2 * st[0] + 3 * st[1]



    st = (num_r, num_b)
    c_player = player1
    while not term_st(st):
        if c_player == 'computer':
            st = getnextmove(st, d)
            print("Computer removed 1 marble from", "red" if st[0] < num_r else "blue", "pile.")
        else:
            print("The Current state is:  ", st)
            p = input("Your turn now! Do you want the red or the blue pile to pick? ")
            while p not in ['red', 'blue'] or (p == 'red' and st[0] == 0) or (p == 'blue' and st[1] == 0):
                p = input("Invalid pile! Please choose between red or blue: ")
            st = (st[0] - 1, st[1]) if p == 'red' else (st[0], st[1] - 1)

        c_player = 'human' if c_player == 'computer' else 'computer'

    win = 'computer' if c_player == 'human' else 'human'
    s = util(st)
    print("Game over, The", win, "won with a score of", s)

if __name__ == '__main__':
    num_r = int(sys.argv[1])
    num_b = int(sys.argv[2])
    player1 = 'computer' if len(sys.argv) < 4 or sys.argv[3] == 'computer' else 'human'
    d = int(sys.argv[4]) if len(sys.argv) == 5 else None
    print(d)
    red_blue_nim(num_r, num_b, player1, d)

