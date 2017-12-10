class State(object):
    board=[]
    row=0
    col=0
    level=2
    score=0
    child=[]
    def __init__(self,board,row,col,level,score,child):
        self.board=board
        self.row=row
        self.col=col
        self.level=level
        self.score=score
        self.child=child

def print_soln(board):
    for temp in board:
        for i in range(0, len(temp), 1):
            if i != len(temp) - 1:
                print temp[i],
            else:
                print temp[i]


def gravity1(board):

    for i in range(0,n,1):
        ind_store = []
        temp_ind = []
        for j in range(n-1,-1,-1):
            if board[j][i]=="*":
                temp_ind.append(j)
                print 'temp_ind',temp_ind
            elif temp_ind!=None:
                ind_store.append(temp_ind)
                temp_ind=[]
        print ind_store
        manipulate=[row[i] for row in board]
        for temp in ind_store:
            print temp[len(temp)-1],temp[0]
            #manipulate=board[i][:]
            print manipulate
            print manipulate[temp[len(temp)-1]:temp[0]+1]
            print manipulate[0:temp[len(temp)-1]]
            board[0:temp[0] + 1]=manipulate[temp[len(temp)-1]:temp[0]+1]+manipulate[0:temp[len(temp)-1]]
            print board



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

    print 'After gravity'
    print_soln(board)
    print ('\n')
    return board


def count_score(fb,r,c):
    print 'Number chosen',r,c
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
        #print 'Explored',explored
    print 'Total_score: ',score
    fruit_board_copy=fb
    for temp in explored:
        fruit_board_copy[temp[0]][temp[1]]='*'
    print 'Fruit Board Copy'
    print_soln(fruit_board_copy)
    print('\n')
    return fruit_board_copy,score
    #return score


def minimax(X,turn):
    print 'Level',X.level
    if X.level == 0:
        return X
    child_list=[]
    for i in range(0,n,1):
        for j in range(0,n,1):
            X_child=copy.deepcopy(X)
            if X_child.board[i][j]!="*":
                #X.board[i][j]="*"
                X_child.row=i
                X_child.col=j
                X_child.level=X.level-1
                new_board, X_child.score = count_score(X_child.board, X_child.row, X_child.col)
                X_child.board=gravity(new_board)
                Obj=State(X_child.board,X_child.row,X_child.col,X_child.level,X_child.score,X_child.child)
                child_list.append(Obj)

    X.child=child_list

    if turn=="computer":
        X.score=-9999999
        for child in X.child:
            print 'child',child.level
            X_child=minimax(child,'opponent')
            print 'Score at level',child.level,' : ',score
            if X_child.score>X.score:
                X.score=X_child.score

        print 'Passing best value: at upper level',X.score
        return X
    else:
        X.score=99999999
        for child in X.child:
            X_child=minimax(child,'computer')
            print 'Score at level', child.level, ' : ', score
            if X_child.score<X.score:
                X.score=X_child.score

        print 'Passing best value: at upper level', X.score
        return X



import random
import time
import copy
import sys
sys.setrecursionlimit(1500)
from collections import deque
child_list=[]
with open('input.txt','r') as f:
    i=1
    fruit_board=[]
    star=[]
    valid_pos=[]
    for line in f:
        #print line
        line=line.strip()
        if line!="":
            if i==1:
                n=int(line)
                #print n
                i+=1
            elif i==2:
                fruit=int(line)
                #print fruit
                i+=1
            elif i==3:
                time_left=float(line)
                #print time_left
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
                #print fruit_board
                i+=1
        else:
            break
print n,fruit,time_left
print fruit_board
#board=[]
row=0
col=0
level=2
score=0
child=[]
good_board=[]
X=State(fruit_board,row,col,level,score,child)
final_X=minimax(X,'computer')
print 'Final Score : ',final_X.score
print_soln(final_X.board)
#row_col=random.choice(valid_pos)
#row_next = random.randint(0, n - 1)
#col_next = random.randint(0, n - 1)
#score=count_score(fruit_board,row_col[0],row_col[1])
