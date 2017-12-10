class State(object):
    board=[]
    row=0
    col=0
    level=3
    score=0
    alpha=-99999999
    beta=99999999
    #child=[]
    def __init__(self,board,row,col,level,score,alpha,beta):
        self.board=board
        self.row=row
        self.col=col
        self.level=level
        self.score=score
        self.alpha = alpha
        self.beta = beta

def print_soln(board,col,row):
    f = open('output.txt', 'w')
    f.write(chr(ord('a') + col - 32))
    f.write(str(row + 1) + '\n')
    for temp in board:
        for i in range(0, len(temp), 1):
            if i != len(temp) - 1:
                f.write(str(temp[i]))
                print temp[i],
            else:
                f.write(str(temp[i]) + '\n')
                print temp[i]

def gravity(board):
    k=-1
    for i in range(0,n,1):
        for j in range(n-1,-1,-1):
            if board[j][i]=="*":
                for k in range(j-1,-1,-1):
                    if board[k][i]!="*":
                        break

                if k!=-1:
                    temp=board[k][i]
                    board[k][i]=board[j][i]
                    board[j][i]=temp

    return board


def count_score(fb,r,c):
    open=deque()
    open.append([r,c])
    explored=[]
    score=1
    while(len(open)):
        [r, c] = open.popleft()
        for i in range(c,n,1):
            if i!=n-1:
                if fb[r][i]==fb[r][i+1] and [r,i+1] not in explored and [r,i+1] not in open:
                    open.append([r,i+1])
                    score+=1
                else:
                    break
        for i in range(c,0,-1):
            if i!=-1:
                if fb[r][i]==fb[r][i-1] and [r,i-1] not in explored and [r,i-1] not in open:
                    open.append([r,i-1])
                    score+=1
                else:
                    break
        for i in range(r,n,1):
            if i!=n-1:
                if fb[i][c]==fb[i+1][c] and [i+1,c] not in explored and [i+1,c] not in open:
                    open.append([i+1,c])
                    score+=1
                else:
                    break
        for i in range(r,0,-1):
            if i!=-1:
                if fb[i][c]==fb[i-1][c] and [i-1,c] not in explored and [i-1,c] not in open:
                    open.append([i-1,c])
                    score+=1
                else:
                    break
        #print 'Open',open
        explored.append([r,c])
    fruit_board_copy=fb
    for temp in explored:
        fruit_board_copy[temp[0]][temp[1]]='*'

    return fruit_board_copy,score*score

def isAllStar(X):
    count=0
    for i in range(0,n,1):
        for j in range(0,n,1):
            if X.board[i][j]=="*":
                count+=1
    if count==n*n:
        #print 'iter count',count
        return True
    else:
        #print 'count',count
        return False
def isAllStar_1(X):
    count=0
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            count+=1
            if X.board[i][j]!="*":
                print 'iter count',count
                return False
    return True

def minimax(X,turn):

    if X.level == 0 or isAllStar(X):
        return X
    best_child= State(X.board, X.row, X.col, X.level, X.score, X.alpha, X.beta)
    best_child.board=list(map(list,X.board))
    best_child.row=X.row
    best_child.col=X.col
    best_child.score=X.score
    best_child.level=X.level
    best_child.alpha=X.alpha
    best_child.beta=X.beta
    score_dict={}
    temp_board= list(map(list, X.board))
    for i in range(0,n,1):
        for j in range(0,n,1):
            if temp_board[i][j]!="*":
                temp_board, score = count_score(temp_board,i,j)
                score_dict[i,j]=score
    ''''
    if turn == "computer":
        score_dict= sorted(score_dict.items(), key=lambda x: (-x[0], x[1]))
    else:
        score_dict = sorted(score_dict.items(), key=lambda x: (x[0], x[1]))
    '''
    score_dict = sorted(score_dict.items(), key=lambda x: (-x[1], x[0]))
    for score in score_dict:
        X_child = State(X.board, X.row, X.col, X.level, X.score, X.alpha, X.beta)
        X_child.board = list(map(list, X.board))
        X_child.row=score[0][0]
        X_child.col=score[0][1]
        X_child.score = score[1]
        X_child.level = X.level-1
        X_child.alpha = X.alpha
        X_child.beta = X.beta
        new_board, X_child.score = count_score(X_child.board, X_child.row, X_child.col)
        X_child.board = gravity(new_board)

        if turn == "computer":
            X_child.score = X.score + X_child.score
        else:
            X_child.score = X.score - X_child.score
        child = State(X_child.board, X_child.row, X_child.col, X_child.level, X_child.score, X_child.alpha,X_child.beta)

        if turn == "computer":
            X_child = minimax(child, 'opponent')
            if X_child.score > best_child.alpha:
                # best_max = X_child.score
                best_child = X_child
                best_child.alpha = X_child.score
                best_child.beta = X.beta
                X.alpha = X_child.score

                if X.level == level - 1:
                    best_child.row = X.row
                    best_child.col = X.col
            if best_child.alpha >= best_child.beta:
                return best_child
                # return X
        else:
            X_child = minimax(child, 'computer')
            if X_child.score < best_child.beta:
                best_child = X_child
                best_child.beta = X_child.score
                best_child.alpha = X.alpha
                X.beta = X_child.score
                if X.level == level - 1:
                    best_child.row = X.row
                    best_child.col = X.col
            if best_child.alpha >= best_child.beta:
                return best_child

    return best_child


###########################################################################################################################################

import sys
import time
sys.setrecursionlimit(1500)
from collections import deque
start_code=time.time()
with open('input.txt','r') as f:
    i=1
    fruit_board=[]
    star=[]
    valid_pos=[]
    for line in f:
        line=line.strip()
        if line!="":
            if i==1:
                n=int(line)
                i+=1
            elif i==2:
                fruit=int(line)
                i+=1
            elif i==3:
                time_left=float(line)
                i+=1
            else:
                arr=[]
                for j in range(len(line)):
                    if line[int(j)] == '*':
                        star.append([int(i-4), int(j)])
                    else:
                        valid_pos.append([int(i-4), int(j)])
                    arr.append(line[int(j)])
                fruit_board.append(arr)
                i+=1
        else:
            break

row=0
col=0
if n<=5:
    set_depth=5
elif n<=10:
    if time_left>15:
        set_depth=4
    elif time_left>10 and time_left<=15:
        set_depth=3
    else:
        set_depth=2

elif n>10 and n<=20:
    if time_left>15:
        set_depth=3
    else:
        set_depth=2

else:
    if time_left>50:
        set_depth=3
    else:
        set_depth=2

level=set_depth
print 'Running at level ',level
score=0
alpha=-99999999
beta=99999999
X=State(fruit_board,row,col,level,score,alpha,beta)
final_X=minimax(X,'computer')

final_board,score = count_score(X.board,final_X.row,final_X.col)
final_X.board=gravity(final_board)

print 'time taken : ',time.time()-start_code
print score
print chr(ord('a') + final_X.col-32),final_X.row+1
print_soln(final_X.board,final_X.col,final_X.row)
