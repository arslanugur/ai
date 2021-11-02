#https://www.hackerrank.com/challenges/botclean

# Head ends here
def posi(n,grid,c):

    pos=[]
    for i in range(n):
        for j in range(n):
            if(grid[i][j]==c):
                pos.append(i)
                pos.append(j)
                break
    return pos

def next_move(posr, posc, board):
    b_pos=[]
    b_pos.append(posr)
    b_pos.append(posc)

    d_pos=posi(5, board, "d")
    
    next=""
    if(b_pos[0]==d_pos[0] and b_pos[1]==d_pos[1]):
        next="CLEAN"
    if(b_pos[0]<d_pos[0]):
        next="DOWN"
    if(b_pos[0]>d_pos[0]):
        next="UP"
    if(b_pos[1]>d_pos[1]):
        next="LEFT"
    if(b_pos[1]<d_pos[1]):
        next="RIGHT"
    print(next)

# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
    
    
