import numpy as np
from collections import deque
searched = set()
s='''111111111111
100010000001
001010111101
111010000101
100001110101
111101010101
100101010101
110101010101
100000000101
111111011101
100000000001
111111101111'''

start='2 0'
finish='11 7'
m= {}

s=s.split('\n')
lines=len(s)
columns=len(s[0])

maze=np.zeros((lines,columns))

for i in range(lines):
    for j in range(columns):
        if s[i][j]=='1':
            maze[i][j]=-1
        else:
            maze[i][j] = 0

for i in range(lines):
    for j in range(columns):
        m[str(i) + ' ' + str(j)]=list()
        if i>0:
            m[str(i)+' '+str(j)].append(str(i-1)+' '+str(j))

        if j<columns-1:
            m[str(i) +' '+ str(j)].append(str(i) +' '+ str(j+1))

        if i<lines-1:
            m[str(i) +' '+ str(j)].append(str(i+1) +' '+ str(j))

        if j>0:
            m[str(i) + ' ' + str(j)].append(str(i) + ' ' + str(j - 1))

def way(position):
    if position==finish:
        return True
    else:
        searched.add(position)
        queue=deque()
        queue+=m[position]
        position_i=int(position.split(' ')[0])
        position_j = int(position.split(' ')[1])
        for next_position in queue:
            if next_position not in searched:
                next_position_i = int(next_position.split(' ')[0])
                next_position_j = int(next_position.split(' ')[1])
                if maze[next_position_i][next_position_j]!=-1:
                    maze[next_position_i][next_position_j]=maze[position_i][position_j]+1
                    way(next_position)

way(start)
print('Кол-во шагов: ',int(maze[int(finish.split(' ')[0])][int(finish.split(' ')[1])]))
searched=set()
print()

def way_back(position):
    if position==start:
        position_i = int(position.split(' ')[0])
        position_j = int(position.split(' ')[1])
        maze[position_i][position_j]=-2
        return True
    else:
        searched.add(position)
        queue=deque()
        queue+=m[position]
        position_i = int(position.split(' ')[0])
        position_j = int(position.split(' ')[1])
        for next_position in queue:
            if next_position not in searched:
                next_position_i = int(next_position.split(' ')[0])
                next_position_j = int(next_position.split(' ')[1])
                if maze[next_position_i][next_position_j]==maze[position_i][position_j]-1:
                    maze[position_i][position_j]=-2
                    way_back(next_position)

way_back(finish)

for i in maze:
    for j in i:
        if j==-2:
            print('*', end=' ')
        elif j==-1:
            print('1',end=' ')
        elif j==0:
            print('0', end=' ')
        else:
            print('0', end=' ')
    print()
