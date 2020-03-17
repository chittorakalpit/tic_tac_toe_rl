import numpy as np


board = np.zeros((3,3))


def next_move(board, r, c, p):
    assert board.shape == (3,3)
    assert r>=0 and r<=2 and c>=0 and c<=2
    assert (np.logical_or(np.logical_or(board == 0, board == 1), board == -1)).all()
    if(board[r,c]==0):
        board[r,c]=p
        return True
    
    return False

def win_condition(board):
    for i in range(3):
        if(board[i,0]==board[i,1] and board[i,0] == board[i,2] and board[i,0] != 0):
            return board[i,0]
    for i in range(3):
        if(board[0,i]==board[1,i] and board[0,i] == board[2,i] and board[0,i] != 0):
            return board[0,i]
    if(board[0,0]==board[1,1] and board[0,0] == board[2,2] and board[0,0] != 0):
        return board[0,0]
    if(board[0,2]==board[1,1] and board[0,2] == board[2,0] and board[2,0] != 0):
        return board[2,0]
    return False

def play_game():
    print("Input player 1's name: ")
    p1 = input()
    print("Input player 2's name: ")
    p2 = input()
    if(p2==p1):
        p1+=" 1"
        p2+=" 2"
        
    board = np.zeros((3,3))
    
    p=1
    win = False
    while(not win):
        print(board)
        if(p==1):
            print("\n\n------- " + p1 + "'s turn " + "-------\n\n")
        else:
            print("\n\n------- " + p2 + "'s turn " + "-------\n\n")
        print("Input row: ")
        r = int(input())
        print("Input column: ")
        c = int(input())
        if(not next_move(board,r,c,p)):
            print("-----!!!!! INVALID MOVE !!!!!-----")
        else:
            p*=-1
            win = win_condition(board)
    print(board)
    if(win==1):
        print("!!!!!!!!!!!!!!!! " + p1 + " wins !!!!!!!!!!!!!!!!")
    else:
        print("!!!!!!!!!!!!!!!! " + p2 + " wins !!!!!!!!!!!!!!!!")
        

if __name__ == '__main__':
    play_game()