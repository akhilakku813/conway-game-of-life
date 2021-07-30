import random
class Cell:
    def __init__(self):
        self.status='dead'
    def make_alive(self):
        self.status='alive'
    def make_dead(self):
        self.status='dead'
    def get_status(self):
        return self.status
    def is_alive(self):
        if self.status=='alive':
            return True
        return False
        
class Grid:
    def __init__(self,rows,cols):
        self.rows=rows
        self.cols=cols
        self.grid=[[Cell() for col in range(cols)] for row in range(rows)]
        
    def set_grid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                i=random.randint(0,2)
                if i==1:
                    self.grid[row][col].make_alive()
    
    def find_next_generation(self):
        temp=[[Cell() for col in range(self.cols)] for row in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                aliveNeighbours=0
                for i in range(-1,2):
                    for j in range(-1,2):
                        if ((row+i)>-1) and ((row+i)<self.rows) and ((col+j)>-1) and ((col+j)<self.cols):
                            if(self.grid[row+i][col+j].is_alive() and not(i==0 and j==0)):
                                aliveNeighbours+=1
                if self.grid[row][col].is_alive():
                    if((aliveNeighbours is 2) or (aliveNeighbours is 3)):
                        temp[row][col].make_alive()
                    else:
                        temp[row][col].make_dead()
                else:
                    if (self.grid[row][col].is_alive()==False) and (aliveNeighbours==3):
                        temp[row][col].make_alive()
                    
        self.grid=temp
    
    def print_grid(self):
        for row in self.grid:
            for col in row:
                if col.is_alive():
                    print('1 ',end='')
                else:
                    print('0 ',end='')
            print()

while True:
    num_rows=int(input('Enter the number of rows:'))
    g=Grid(num_rows,num_rows)
    g.set_grid()
    g.print_grid()

    while True:
        choice=input('Press Enter for continue, r for restart: ')
        if choice not in ['','r']:
            continue
        if choice=='r':
            break
        print('------------Next Generation-------------\n')
        g.find_next_generation()
        g.print_grid()
    go=input('Press y to play again, any other key to quit: ')
    if go=='y':
        continue
    else:
        quit()