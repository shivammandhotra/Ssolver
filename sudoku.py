#import numpy as np 
sudoku=[[0,4,2,6,0,0,0,0,3],
       [0,0,0,0,0,0,7,0,0],
       [5,3,8,0,0,1,6,0,2],
       [0,0,5,0,0,9,0,7,0],
       [0,0,0,8,0,6,0,0,0],
       [0,2,0,7,0,0,1,0,0],
       [8,0,4,1,0,0,2,3,6],
       [0,0,1,0,0,0,0,0,0],
       [3,0,0,0,0,2,8,9,0]]
#print(sudoku)

def possible(y,x,n):
      global sudoku
      for i in range(0,9):
            if sudoku[y][i]==n:
                  return False
      for i in range(0,9):
            if sudoku[i][x]==n:
                  return False
      x0=(x//3)*3
      y0=(y//3)*3
      for i in range(0,3):
            for j in range(0,3):
                  if sudoku[y0+i][x0+j]==n:
                        return False
      return True

def solver():
     global sudoku
     for x in range(0,9):
           for y in range(0,9):
                 if sudoku[x][y]==0:
                       for n in range(1,10):
                             if possible(x,y,n):
                                   sudoku[x][y]=n
                                   solver()
                                   sudoku[x][y]=0
                                   return
                        
      print(sudoku)                  
 
