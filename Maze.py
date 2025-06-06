from Cells import Cell
import time
import random

class Maze():
    def __init__(self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
        seed = None):

        self.__x1 = x1
        self.__y1 = y1
        self.__rows = num_rows
        self.__cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        if seed:
            random.seed(seed)
        

        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0,0)
        self.__reset_cells_visited()

    def __create_cells(self):
        
        for i in range(self.__cols):
            row = []
            for j in range(self.__rows):
                row.append(Cell(self.__win))
            self.__cells.append(row)
        
        for i in range(self.__cols):
            for j in range(self.__rows):
                self.__draw_cell(i,j)

    def __draw_cell(self,i,j):
        if self.__win is None:
            return

        x1 = self.__cell_size_x * i + self.__cell_size_x
        x2 = x1 + self.__cell_size_x
        y1 =self.__cell_size_y * j + self.__cell_size_y
        y2 = y1 + self.__cell_size_y

        self.__cells[i][j].draw(x1,x2,y1,y2)
        self.__animate()

    def __animate(self):
        if self.__win is None:
            return
        
        self.__win.redraw()
        time.sleep(0.05)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0,0)
        self.__cells[self.__cols-1][self.__rows-1].has_bottom_wall = False
        self.__draw_cell(self.__cols-1,self.__rows-1)

    def __break_walls_r(self,i,j):
        self.__cells[i][j].visited = True

        while True:
            to_visit = []
    
            #right
            if i < self.__cols -1 and not self.__cells[i+1][j].visited:
                to_visit.append([i+1,j])
            #left
            if i > 0 and not self.__cells[i-1][j].visited:
                to_visit.append([i-1,j])
            
            #up
            if j > 0 and not self.__cells[i][j-1].visited:
                to_visit.append([i,j-1])

            #down
            if j < self.__rows -1 and not self.__cells[i][j+1].visited:
                to_visit.append([i,j+1])


            if len(to_visit) == 0:
                self.__draw_cell(i,j)
                return

            
            direction = to_visit[random.randrange(len(to_visit))]

            if direction[0] == i+1:
                self.__cells[i][j].has_right_wall = False
                self.__cells[i+1][j].has_left_wall = False
                
            if direction[0] == i-1:
                self.__cells[i][j].has_left_wall = False
                self.__cells[i-1][j].has_right_wall = False
                

            if direction[1] == j+1:
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[i][j+1].has_top_wall = False
                

            if direction[1] == j-1:
                self.__cells[i][j].has_top_wall = False
                self.__cells[i][j-1].has_bottom_wall = False
                


            self.__break_walls_r(direction[0],direction[1])

    def __reset_cells_visited(self):
        for i in range(self.__cols):
            for j in range(self.__rows):
                self.__cells[i][j].visited = False

    def solve(self):
        return self.__solve_r(0,0)
    
    def __solve_r(self, i,j):
        self.__animate()


        self.__cells[i][j].visited = True

        if j == self.__rows - 1 and i == self.__cols - 1:
            return True
        
        #move right
        if i < self.__cols - 1 and not self.__cells[i][j].has_right_wall and not self.__cells[i+1][j].visited :
            self.__cells[i][j].draw_move(self.__cells[i+1][j])
            if self.__solve_r(i+1,j):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i+1][j], True)

        #move left
        if i > 0 and not self.__cells[i][j].has_left_wall and not self.__cells[i-1][j].visited:
            self.__cells[i][j].draw_move(self.__cells[i-1][j])
            if self.__solve_r(i-1,j):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i-1][j], True)


        #move up
        if j > 0 and not self.__cells[i][j].has_top_wall and not self.__cells[i][j-1].visited :
            self.__cells[i][j].draw_move(self.__cells[i][j-1])
            if self.__solve_r(i,j-1):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i][j-1], True)

        #move down
        if j < self.__rows -1 and not self.__cells[i][j].has_bottom_wall and not self.__cells[i][j+1].visited :
            self.__cells[i][j].draw_move(self.__cells[i][j+1])
            if self.__solve_r(i,j+1):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i][j+1], True)

        return False