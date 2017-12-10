class State(object):
    board=[]
    row=0
    col=0
    level=2
    score=0

    def __init__(self,board,row,col,level,score):
        self.board=board
        self.row=row
        self.col=col
        self.level=level
        self.score=score

def print_soln(board):
    for temp in board:
        for i in range(0, len(temp), 1):
            if i != len(temp) - 1:
                print temp[i],
            else:
                print temp[i]
    return

def print_soln_write(board,col,row):
    f = open('output.txt', 'w')
    f.write(chr(ord('a')+col-32))
    f.write(str(row+1)+'\n')
    for temp in board:
        for i in range(0, len(temp), 1):
            if i != len(temp) - 1:
                # z = str(temp[i])
                f.write(str(temp[i]))
                # print temp[i],
            else:
                f.write(str(temp[i]) + '\n')


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
    print 'Total_score: ',score*score
    fruit_board_copy=fb
    for temp in explored:
        fruit_board_copy[temp[0]][temp[1]]='*'
    print 'Fruit Board Copy'
    print_soln(fruit_board_copy)
    print('\n')
    return fruit_board_copy,score*score
    #return score

def isAllStar(X):
    count=0
    for i in range(0,n,1):
        for j in range(0,n,1):
            if X.board[i][j]=="*":
                count+=1
    if count==n*n:
        return True
    else:
        return False

def minimax(X,turn):
    global child_count

    #print "BAAAAP",X.board
    print 'Level',X.level
    if X.level == 0 or isAllStar(X):
        return X
    best_min = 99999
    best_max = -99999
    best_child = copy.deepcopy(X)
    for i in range(0,n,1):
        for j in range(0,n,1):
            X_child=copy.deepcopy(X)

            if X_child.board[i][j]!="*":
                child_count += 1
                X_child.row=i
                X_child.col=j
                X_child.level=X.level-1
                new_board, X_child.score = count_score(X_child.board, X_child.row, X_child.col)
                X_child.board=gravity(new_board)

                if turn == "computer":
                    X_child.score=X.score + X_child.score
                    print 'child score',X_child.score
                else:
                    X_child.score = X.score - X_child.score
                    print 'child score',X_child.score

                #child=State(X_child.board,X_child.row,X_child.col,X_child.level,X_child.score)

                if turn == "computer":
                    X_child = minimax(X_child, 'opponent')
                    print 'Score at level', X_child.level, ' : ',X_child.score
                #    X_child.score = X.score + X_child.score
                    if X_child.score > best_max:
                        best_max = X_child.score
                        best_child = X_child
                        if X.level==level-1:
                            best_child.row = X.row
                            best_child.col = X.col

                    #print 'Best Child-----------------', X_child.board, 'from ', X_child.row, X_child.col
                    #print 'Passing best value: at upper level', X.score
                    # return X
                else:

                    X_child = minimax(X_child, 'computer')
                    print 'Score at level', X_child.level, ' : ', X_child.score
                 #   X_child.score = X.score - X_child.score
                    if X_child.score < best_min:
                        best_min = X_child.score
                        best_child = X_child
                        if X.level==level-1:
                            best_child.row = X.row
                            best_child.col = X.col

                    #print 'Passing best value: at upper level', X.score
    return best_child


import random
import time
import copy
import sys
sys.setrecursionlimit(1500)
from collections import deque
child_list=[]
iterations=0
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
level=3
score=0
child_count=0
X=State(fruit_board,row,col,level,score)
final_X=minimax(X,'computer')
print 'Final Score : ',final_X.score
#print_soln(final_X.board)
print final_X.row,final_X.col
final_board,score = count_score(X.board,final_X.row,final_X.col)
final_X.board=gravity(final_board)
print chr(ord('a') + final_X.col-32),final_X.row+1
print_soln(final_X.board)
print child_count
print_soln_write(final_X.board,final_X.col,final_X.row)
