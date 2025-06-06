from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, height, width):
        
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg='white', width = width, height = height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print('Window is closed')

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_colour='black'):
        line.Draw(self.__canvas, fill_colour)
        

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Line():
    def __init__(self,point_1, point_2):
        self.x1 = point_1.x
        self.x2 = point_2.x
        self.y1 = point_1.y
        self.y2 = point_2.y

    def Draw(self,canvas, fill_colour='black'):
        canvas.create_line(self.x1,self.y1,self.x2,self.y2, fill = fill_colour,width=2)
        
        




