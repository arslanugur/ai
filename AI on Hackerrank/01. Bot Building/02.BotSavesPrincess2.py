# https://www.hackerrank.com/challenges/saveprincess2

def pos(n,grid,c):
    pos=[]
    for i in range(n):
        for j in range(n):
            if(grid[i][j]==c):
                pos.append(i)
                pos.append(j)
                break
    return pos
def nextMove(n,r,c,grid):
    p_pos=pos(n,grid,"p")
    m_pos=[]
    m_pos.append(r)
    m_pos.append(c)

    next=""

    if(m_pos[0]<p_pos[0]):
        next="DOWN"
    if(m_pos[0]>p_pos[0]):
        next="UP"
    if(m_pos[1]>p_pos[1]):
        next="LEFT"
    if(m_pos[1]<p_pos[1]):
        next="RIGHT"
    return next

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))

