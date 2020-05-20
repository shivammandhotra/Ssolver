#import numpy as np 
grid=[[0,4,2,6,0,0,0,0,3],
      [0,0,0,0,0,0,7,0,0],
      [5,3,8,0,0,1,6,0,2],
      [0,0,5,0,0,9,0,7,0],
      [0,0,0,8,0,6,0,0,0],
      [0,2,0,7,0,0,1,0,0],
      [8,0,4,1,0,0,2,3,6],
      [0,0,1,0,0,0,0,0,0],
      [3,0,0,0,0,2,8,9,0]]
#print(grid)
'''import numpy as np
print(n p.matrix(grid))'''
def possible(y,x,n):
      global grid
      for i in range(0,9):
            if grid[y][i]==n:
                  return False
      for i in range(0,9):
            if grid[i][x]==n:
                  return False
      x0=(x//3)*3
      y0=(y//3)*3
      for i in range(0,3):
            for j in range(0,3):
                  if grid[y0+i][x0+j]==n:
                        return False
      return True
print(possible(4,4,3) )
                                               