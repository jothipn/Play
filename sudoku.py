import numpy as np

grid = [[0,9,0,1,0,6,5,0,0],
        [0,0,5,0,0,4,0,0,0],
        [0,0,2,5,3,0,0,6,7],
        [2,5,0,0,0,0,0,0,9],
        [0,0,0,2,9,5,1,8,6],
        [0,0,0,0,0,0,0,0,5],
        [0,1,7,0,6,8,0,0,0],
        [0,0,6,0,0,0,9,7,0], #Lats but 1 7
        [0,0,0,4,0,7,6,0,8]] #Last 8

print (np.matrix(grid))

def possible(y,x, n):
    global grid
    for i in range (0,9):
        if grid[y][i] == n:
            return False
    for i in range (0,9):
        if grid[i][x] == n:
            return False
    x0 = (x//3) * 3
    y0 = (y//3) * 3
    for i in range (0,3):
        for j in range (0,3):
            if grid[y0+i][x0 + j] == n:
                return False
    
    return True

def solve():
    global grid

    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                flag = True
                for n in range (1, 10):
                    if (possible(i, j, n)):
                        grid[i][j] = n
                        solve()
                        grid[i][j] = 0
                return

    print(np.matrix(grid))
    input ("More?")

solve()    
            
    


            
