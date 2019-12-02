'''PlayerSkeleton.py
A bare-bones agent that plays Toro-Tile Straight,
but rather poorly.

To create your own agent, make a copy of this file, using
the naming convention YourUWNetID_TTS_agent.py.

If you need to import additional custom modules, use
a similar naming convention... e.g.,
YourUWNetID_TTS_custom_static.py


'''

from TTS_State import TTS_State
import random

import TTS_State as tt
USE_CUSTOM_STATIC_EVAL_FUNCTION = False
global turn_c,who_i
turn_c = 0

class MY_TTS_State(TTS_State):
    def static_eval(self):
        if USE_CUSTOM_STATIC_EVAL_FUNCTION:
            return self.custom_static_eval()
        else:
            return self.basic_static_eval()

    def basic_static_eval(self):
        H = len(self.board)  # height of board = num. of rows
        W = len(self.board[0])  # width of board = num. of cols.
        # print(self.board)
        TWF = 0
        TBF = 0
        Directions = [(-1, -1), (-1, 0), (-1, 2), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]  # E, NE, N, NW
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 'W':
                    for di in range(8):  #
                        dp = Directions[di]
                        new_i = i
                        new_j = j
                        new_i += dp[0]
                        if new_i < 0:
                            new_i = H - 1
                        if new_i >= H:
                            new_i = 0  # toroidal wrap
                        new_j += dp[1]
                        if new_j < 0:
                            new_j = H - 1
                        if new_j >= H:
                            new_j = 0
                        if self.board[new_i][new_j] == ' ': TWF += 1

                        # print(self.board[i][j],TWF)


                if self.board[i][j] == 'B':
                    for di in range(8):  #
                        dp = Directions[di]
                        new_i = i
                        new_j = j
                        new_i += dp[0]
                        if new_i < 0:
                            new_i = H - 1
                        if new_i >= H:
                            new_i = 0  # toroidal wrap
                        new_j += dp[1]
                        if new_j < 0:
                            new_j = H - 1
                        if new_j >= H:
                            new_j = 0
                        if self.board[new_i][new_j] == ' ': TBF += 1

                        # print(self.board[i][j],TBF)

        score = TWF - TBF
        return score

    def custom_static_eval(self):
        H = len(self.board)  # height of board = num. of rows
        W = len(self.board[0])  # width of board = num. of cols.
        #print(self.board)
        TWF = 0
        TBF = 0
        Directions = [(-1, -1), (-1, 0), (-1, 2), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]  # E, NE, N, NW
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                w_c = [0,0,0,0,0,0,0,0]
                b_c = [0,0,0,0,0,0,0,0]
                if self.board[i][j] == 'W':
                    for di in range(8):  #
                        dp = Directions[di]
                        new_i = i
                        new_j = j
                        new_i += dp[0]
                        if new_i < 0:
                            new_i = H-1
                        if new_i >= H:
                            new_i = 0  # toroidal wrap
                        new_j += dp[1]
                        if new_j < 0:
                            new_j = H - 1
                        if new_j >= H:
                            new_j = 0
                        if self.board[new_i][new_j] == ' ': TWF += 1
                        if self.board[new_i][new_j] == 'W': TWF += 10
                        if self.board[new_i][new_j] == 'W': w_c[di]=1
                        # print(self.board[i][j],TWF)
                    if (w_c[0] == 1 and w_c[7] == 1) or (w_c[1] == 1 and w_c[6] == 1) or \
                        (w_c[2] == 1 and w_c[5] == 1) or (w_c[3] == 1 and w_c[4] == 1):
                        TWF += 50
                    if (w_c[0] == 1 and w_c[1] == 1 and w_c[2] == 1) or (w_c[2] == 1 and w_c[4] == 1 and w_c[7] == 1) or \
                        (w_c[5] == 1 and w_c[6] == 1 and w_c[7] == 1) or (w_c[0] == 1 and w_c[3] == 1 and w_c[5] == 1):
                        TWF += 100

                if self.board[i][j] == 'B':
                    for di in range(8):  #
                        dp = Directions[di]
                        new_i = i
                        new_j = j
                        new_i += dp[0]
                        if new_i < 0:
                            new_i = H - 1
                        if new_i >= H:
                            new_i = 0  # toroidal wrap
                        new_j += dp[1]
                        if new_j < 0:
                            new_j = H - 1
                        if new_j >= H:
                            new_j = 0
                        if self.board[new_i][new_j] == ' ': TBF += 1
                        if self.board[new_i][new_j] == 'B': TBF += 10
                        if self.board[new_i][new_j] == 'B': b_c[di] = 1
                        # print(self.board[i][j],TBF)
                    if (b_c[0] == 1 and b_c[7] == 1) or (b_c[1] == 1 and b_c[6] == 1) or \
                        (b_c[2] == 1 and b_c[5] == 1) or (b_c[3] == 1 and b_c[4] == 1):
                        TBF += 50
                    if (b_c[0] == 1 and b_c[1] == 1 and b_c[2] == 1) or (b_c[2] == 1 and b_c[4] == 1 and b_c[7] == 1) or \
                        (b_c[5] == 1 and b_c[6] == 1 and b_c[7] == 1) or (b_c[0] == 1 and b_c[3] == 1 and b_c[5] == 1):
                        TBF += 100
        score = TWF - TBF
        return score


# The following is a skeleton for the function called parameterized_minimax,
# which should be a top-level function in each agent file.
# A tester or an autograder may do something like
# import ABC_TTS_agent as player, call get_ready(),
# and then it will be able to call tryout using something like this:
# results = player.parameterized_minimax(**kwargs)
from collections import defaultdict
def tree():
    return defaultdict(tree)
import copy
def parameterized_minimax(
        current_state=None,
        max_ply=4,
        alpha_beta=False,
        use_custom_static_eval_function=True):
    # All students, add code to replace these default
    # values with correct values from your agent (either here or below).
    cutoff = 0
    who = 'B'
    if current_state.whose_turn == who:
        who = 'W'
    if turn_c == 0:
        who = who_i
    #print('wwwwwwwwwwww',who,who_i)
    go = 0
    lst = [[current_state]]
    while go < max_ply:
        alst = []
        states = lst[go]
        for x in range(len(states)):
            for y in range(len(states[x].board)):
                for z in range(len(states[x].board[0])):
                    if states[x].board[y][z] == ' ':
                        #n_vac+=1
                        board = copy.deepcopy(states[x].board)
                        board[y][z] = who
                        new_s =  MY_TTS_State(board)
                        #print(who,go,x,y,z,board,states[x].board)
                        alst.append(new_s)
        lst.append(alst)
        go += 1
        if who == 'W':
            who = 'B'
        else:
            who = 'W'
    alpha = float('-inf')
    beta = float('inf')
    value_tree = copy.deepcopy(lst)
    prune_tree = copy.deepcopy(lst)
    if use_custom_static_eval_function:
        for i in range(len(lst[-1])):
            value_tree[-1][i] = lst[-1][i].custom_static_eval()
    else:
        for i in range(len(lst[-1])):
            value_tree[-1][i] = lst[-1][i].basic_static_eval()
    #print(len(value_tree))
    if not alpha_beta:
        for i in range(len(value_tree)-2,-1,-1):
            factor = int(len(value_tree[i+1])/len(value_tree[i]))
            for j in range(len(value_tree[i])):
                if current_state.whose_turn == 'B':
                    #print(j,len(value_tree[i]),j*(len(value_tree[i])-1),j*(len(value_tree[i])-1)+(len(value_tree[i])-2))
                    if i != 0:
                        if i % 2 == 0:
                            value_tree[i][j] = max([value_tree[i+1][x] for x in range(j*factor,j*factor+factor-1,1)])
                        else:
                            value_tree[i][j] = min([value_tree[i + 1][x] for x in range(j*factor,j*factor+factor-1,1)])
                    else:
                        value_tree[i][j] = max(value_tree[i+1])
                else:
                    if i != 0:
                        if i % 2 == 0:
                            value_tree[i][j] = min(
                                [value_tree[i + 1][x] for x in range(j * factor, j * factor + factor - 1, 1)])
                        else:
                            value_tree[i][j] = max(
                                [value_tree[i + 1][x] for x in range(j * factor, j * factor + factor - 1, 1)])
                    else:
                        value_tree[i][j] = min(value_tree[i + 1])
    else:
        for i in range(len(value_tree)-2,-1,-1):
            factor = int(len(value_tree[i+1])/len(value_tree[i]))
            for j in range(len(value_tree[i])):
                if current_state.whose_turn == 'B':
                    #print(j,len(value_tree[i]),j*(len(value_tree[i])-1),j*(len(value_tree[i])-1)+(len(value_tree[i])-2))
                    if i != 0:
                        if i % 2 == 0:
                            value_tree[i][j] = max([value_tree[i+1][x] for x in range(j*factor,j*factor+factor-1,1)])
                        else:
                            value_tree[i][j] = min([value_tree[i + 1][x] for x in range(j*factor,j*factor+factor-1,1)])
                    else:
                        value_tree[i][j] = max(value_tree[i+1])
                else:
                    if i != 0:
                        if i % 2 == 0:
                            value_tree[i][j] = min(
                                [value_tree[i + 1][x] for x in range(j * factor, j * factor + factor - 1, 1)])
                        else:
                            #print(len(lst[-1]),'lst-1',lst)
                            value_tree[i][j] = max(
                                [value_tree[i + 1][x] for x in range(j * factor, j * factor + factor - 1, 1)])
                    else:
                        value_tree[i][j] = min(value_tree[i + 1])

        for i in range(len(value_tree) - 2, 0, -1):
            for j in range(len(value_tree[i])):
                if current_state.whose_turn == 'W':
                    if i % 2 == 0:
                        if value_tree[i][j] >= value_tree[i][0]:
                            cutoff += 1
                    else:
                        if value_tree[i][j] <= value_tree[i][0]:
                            cutoff += 1
                if current_state.whose_turn == 'B':
                    if i % 2 == 0:
                        if value_tree[i][j] <= value_tree[i][0]:
                            cutoff += 1
                    else:
                        if value_tree[i][j] >= value_tree[i][0]:
                            cutoff += 1
        #print(cutoff)

    #print(value_tree)
    #make move based on search
    if len(value_tree)>1:
        for i in range(len(value_tree[1])):
            if value_tree[0][0] == value_tree[1][i]:
                move = lst[1][i]
    else:
        move = lst[0][0]
        #print(max_ply,move.board,'--------------')
    #print(move.board)
    #count expand notes
    expand = 0
    for i in range(1,len(lst)):
        expand += len(lst[i])
    #print(expand)
    DATA = {}
    DATA['CURRENT_STATE'] = move
    DATA['CURRENT_STATE_STATIC_VAL'] = move.static_eval()
    DATA['N_STATES_EXPANDED'] = len(lst)
    DATA['N_STATIC_EVALS'] = len(lst)
    DATA['N_CUTOFFS'] = cutoff
    return DATA




    # for i in range(len(lst)-1, -1, -1):
    #     for j in range(len(lst[i])):
    #         if i == len(lst)-1:#if i is the last item in lst, do not need to set alpha beta
    #             value_tree[i][j] = lst[i][j].static_eval()
    #         else:
    #             prune_tree[i][j] = [alpha, beta]
    #             if lst[i][j].whose_turn == 'W':











    # STUDENTS: You may create the rest of the body of this function here.

    # Actually return all results...



def take_turn(current_state, last_utterance, time_limit):
    # Compute the new state for a move.
    # Start by copying the current state.
    global turn_c, who_i
    current_state._class_ = MY_TTS_State
    new_state = MY_TTS_State(current_state.board)
    # Fix up whose turn it will be.
    who = current_state.whose_turn
    new_who = 'B'
    if who == 'B':
        new_who = 'W'
    new_state.whose_turn = new_who

    # Place a new tile
    location = _find_next_vacancy(new_state.board)
    if location == False: return [[False, current_state], "I don't have any moves!"]
    blank = 0
    for i in range(len(new_state.board)):
        for j in range(len(new_state.board[0])):
            if new_state.board[i][j] == ' ':
                blank += 1



    max_ply = 2
    if blank <= max_ply:
        new = parameterized_minimax(new_state, max_ply=blank-1)['CURRENT_STATE']
    else:
        new = parameterized_minimax(new_state, max_ply=max_ply)['CURRENT_STATE']

    move_c = ()
    new_state.board = new.board
    van_c = 0
    for i in range(len(new_state.board)):
        for j in range(len(new_state.board[0])):
            if current_state.board[i][j] == ' ':
                van_c+=1
            if new_state.board[i][j] != current_state.board[i][j]:
                move_c = (i,j)

    if van_c == 1:
        move_c = _find_next_vacancy(current_state.board)
        #print('in2')

    # Construct a representation of the move that goes from the
    # currentState to the newState.

    # Make up a new remark
    sentences = ['Nice move!', 'This is taking too long. Let\'s end this quick.', 'I am not really good at playing games but I will try my best.',\
                 'I think I made a decent move.', 'I think I will win this.', 'Release the Kraken!', 'I will buy you a coffee if you let me win :)',\
                    'Go easy on me, I am new here.', 'Do you want to listen to my music?', 'Let\'s ROCK!']
    test_state = MY_TTS_State(current_state.board)
    if new_who == 'W' and test_state.custom_static_eval()<0:
        new_utterance = 'Look at you! Nice move!'
    if sentences:
        new_utterance = random.choice(sentences)
        sentences.remove(new_utterance)
    else:
        new_utterance = 'I am too tried to talk.'
    #print(new_utterance)
    turn_c += 1
    #print(move_c,new_state.board)
    return [[move_c, new_state], new_utterance]


def _find_next_vacancy(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == ' ': return (i, j)
    return False


def moniker():
    return "Birdie"  # Return your agent's short nickname here.


def who_am_i():
    return """My name is Birdie, created by Tianyi Zhang.
I am a punk rocker with a mohawk. I consider myself to be an aggressive line-blocker."""


def get_ready(initial_state, k, who_i_play, player2Nickname):
    initial_state._class_ = MY_TTS_State
    global who_i
    who_i = who_i_play

    # do any prep, like eval pre-calculation, here.
    #parameterized_minimax(initial_state)

    return "OK"
# if __name__ == "__main__":
#     board = [
#         ['-', '-', '-', '-'],
#         ['-', 'W', ' ', '-'],
#         ['-', ' ', ' ', '-'],
#         ['-', '-', '-', '-'], ]
#     new = MY_TTS_State(board,whose_turn='B')
#     lst = parameterized_minimax(new)
# #     print(lst[0][0].board)
# #     new = MY_TTS_State(TTS_State(tt.INITIAL_BOARD))
# #     score = new.static_eval()