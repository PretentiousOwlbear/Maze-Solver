from graphics import Line, Point

class Cell():
    def __init__(self, window= None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window
        self.visited = False

    def draw(self, x1,x2,y1,y2):
        if self.__win is None:
            return None
        
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        if self.has_left_wall:
            self.__win.draw_line(Line(Point(self.__x1,self.__y1),Point(self.__x1,self.__y2)))
        else:
            self.__win.draw_line(Line(Point(self.__x1,self.__y1),Point(self.__x1,self.__y2)), 'white')

        if self.has_right_wall:
            self.__win.draw_line(Line(Point(self.__x2,self.__y1),Point(self.__x2,self.__y2)))
        else:
            self.__win.draw_line(Line(Point(self.__x2,self.__y1),Point(self.__x2,self.__y2)), 'white')

        if self.has_top_wall:
            self.__win.draw_line(Line(Point(self.__x1,self.__y1),Point(self.__x2,self.__y1)))
        else:
            self.__win.draw_line(Line(Point(self.__x1,self.__y1),Point(self.__x2,self.__y1)), 'white')

        if self.has_bottom_wall:
            self.__win.draw_line(Line(Point(self.__x1,self.__y2),Point(self.__x2,self.__y2)))
        else:
            self.__win.draw_line(Line(Point(self.__x1,self.__y2),Point(self.__x2,self.__y2)), 'white')


    def draw_move(self,to_cell, undo=False):
        if self.__win is None:
            return None

        fill_colour = 'red'
        if undo:
            fill_colour = 'gray'
            
        
        mid_cell1 = Point(self.__x1 + abs(self.__x2-self.__x1)//2, self.__y1 + abs(self.__y2-self.__y1)//2)
        mid_cell2 = Point(to_cell.__x1 + abs(to_cell.__x2-to_cell.__x1)//2, to_cell.__y1 + abs(to_cell.__y2-to_cell.__y1)//2)
        line = Line(mid_cell1,mid_cell2)

        self.__win.draw_line(line, fill_colour)