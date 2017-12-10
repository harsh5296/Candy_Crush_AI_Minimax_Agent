class State(object):
    board=[]
    row=0
    col=0
    level=3
    score=0
    alpha=-9999
    beta=99999
    #child=[]
    def __init__(self,board,row,col,level,score,alpha,beta):
        self.board=board
        self.row=row
        self.col=col
        self.level=level
        self.score=score
        self.alpha = alpha
        self.beta = beta
        #self.child=child

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
'''

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

'''

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

    #print 'After gravity'
    #print_soln(board)
    #print ('\n')
    return board


def count_score(fb,r,c):
    #print 'Number chosen',r,c
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
    #print 'Total_score: ',score*score
    fruit_board_copy=fb
    for temp in explored:
        fruit_board_copy[temp[0]][temp[1]]='*'
    #print 'Fruit Board Copy'
    #print_soln(fruit_board_copy)
    #print('\n')
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

    #print 'Level',X.level
    global prune
    global child_count
    if X.level == 0 or isAllStar(X):
        return X
    best_min = 99999
    best_max = -99999
    #best_child = json.loads(json.dumps(X))
    #best_child = cPickle.loads(cPickle.dumps(X, -1))
    best_child= State(X.board, X.row, X.col, X.level, X.score, X.alpha, X.beta)
    best_child.board=list(map(list,X.board))
    best_child.row=X.row
    best_child.col=X.col
    best_child.score=X.score
    best_child.level=X.level
    best_child.alpha=X.alpha
    best_child.beta=X.beta
    #best_child=msgpack.unpackb(msgpack.packb(X))
    #best_child = copy(X)
    #best_child = copy.deepcopy(X)
    for i in range(0,n,1):
        for j in range(0,n,1):
            #X_child=copy.deepcopy(X)
            #X_child=cPickle.loads(cPickle.dumps(X, -1))
            #global child_count
            #child_count+=1
            X_child = State(X.board, X.row, X.col, X.level, X.score, X.alpha, X.beta)
            X_child.board = list(map(list, X.board))
            X_child.row = X.row
            X_child.col = X.col
            X_child.score = X.score
            X_child.level = X.level
            X_child.alpha = X.alpha
            X_child.beta = X.beta

            if X_child.board[i][j]!="*":
                #X.board[i][j]="*"
                child_count += 1
                X_child.row=i
                X_child.col=j
                X_child.level=X.level-1
                new_board, X_child.score = count_score(X_child.board, X_child.row, X_child.col)
                X_child.board=gravity(new_board)
                if turn == "computer":
                    X_child.score=X.score + X_child.score
                    #print 'child score',X_child.score
                else:
                    X_child.score = X.score - X_child.score
                    #print 'child score',X_child.score
                child=State(X_child.board,X_child.row,X_child.col,X_child.level,X_child.score,X_child.alpha,X_child.beta)

                #child_list.append(Obj)
                if turn == "computer":
                    #X.score = -9999999
                    #for child in X.child:
                    #print 'child', child.level
                    X_child = minimax(child, 'opponent')
                    #print 'Score at level', X_child.level, ' : ',X_child.score

                    if X_child.score > best_child.alpha:
                        #best_max = X_child.score
                        best_child = X_child
                        best_child.alpha=X_child.score
                        best_child.beta=X.beta
                        X.alpha=X_child.score
                        if X.level==level-1:
                            best_child.row = X.row
                            best_child.col = X.col
                    #print 'Best ALpha Beta', best_child.alpha,best_child.beta
                    if best_child.alpha>=best_child.beta:
                        #print 'now pruning'
                        #global prune
                        prune=prune+1
                        return best_child
                    #print 'Best Child-----------------', X_child.board, 'from ', X_child.row, X_child.col
                    #print 'Passing best value: at upper level', X.score
                    # return X
                else:
                    #X.score = 99999999
                    #for child in X.child:
                    X_child = minimax(child, 'computer')
                    #print 'Score at level', X_child.level, ' : ', X_child.score

                    if X_child.score < best_child.beta:
                        #best_min = X_child.score
                        best_child = X_child
                        best_child.beta=X_child.score
                        best_child.alpha=X.alpha
                        X.beta=X_child.score
                        if X.level==level-1:
                            best_child.row = X.row
                            best_child.col = X.col
                        #print 'Passing best value: at upper level', X.score
                    #print 'Best ALpha Beta', best_child.alpha, best_child.beta
                    if best_child.alpha >= best_child.beta:
                        #print 'now pruning'
                        #global prune
                        prune+=1
                        return best_child
    #print child_count,prune
    return best_child


import random
import time
import copy
import sys
import time
#import json
#import timeit
#import cPickle
#import msgpack
child_count=0
prune=0
sys.setrecursionlimit(1500)
from collections import deque
#child_list=[]
start_code=time.time()
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

row=0
col=0
level=3
score=0
alpha=-99999
beta=99999
X=State(fruit_board,row,col,level,score,alpha,beta)
final_X=minimax(X,'computer')

final_board,score = count_score(X.board,final_X.row,final_X.col)
final_X.board=gravity(final_board)

print 'time taken : ',time.time()-start_code
print score
print chr(ord('a') + final_X.col-32),final_X.row+1
print_soln(final_X.board,final_X.col,final_X.row)
