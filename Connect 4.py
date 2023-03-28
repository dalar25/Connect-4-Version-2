from tkinter import *
import tkinter.messagebox

class Connect4Label(Label):
 
    def __init__(self,master,coord):
        Label.__init__(self,bg='white',width=8,height=4,text='',borderwidth=1,relief='sunken')
        # above line taken from https://www.delftstack.com/howto/python-tkinter/how-to-set-border-of-tkinter-label-widget/
        #https://docs.python.org/3/library/tkinter.html
        #https://stackoverflow.com/questions/42942534/how-to-change-the-color-of-a-tkinter-label-programmatically/42942622
        self.coord = coord
        self.master = master
        self.filled = False
        self.redFilled = False
        self.yellowFilled = False

    def get_filled(self):
        return self.filled

    def get_red_filled(self):
        return self.redFilled

    def get_yellow_filled(self):
        return self.yellowFilled
    
    def get_coord(self):
        return self.coord

    def fill(self,turn):
        self.filled = True
        if turn == True:
            self['bg']='red' #https://stackoverflow.com/questions/42942534/how-to-change-the-color-of-a-tkinter-label-programmatically/42942622
            self.redFilled = True
        else:
            self['bg']='yellow' #https://stackoverflow.com/questions/42942534/how-to-change-the-color-of-a-tkinter-label-programmatically/42942622
            self.yellowFilled = True
        self.master.change_turn()

        
class Connect4Button(Button):
    '''represents a Connect 4 Cell'''

    def __init__(self,master,coord):
        '''creates a new blank ConnectCell with (row,column) coord'''
        Button.__init__(self,width=3,height=2,text='',font = ('Arial',24)) #sets up the cell
        self.coord = coord  # (row,column) coordinate tuple
        self.master = master #master
        self.bind('<Button-1>',self.play_turn)

    def fill(self,event):
        self['text'] = 5
        self.filled = True
        self.locked = False

    def play_turn(self, turn):
        self.master.play_turn(self.coord[0])

class ConnectGrid(Frame):
    '''Creates the Connect 4 Grid'''

    def __init__(self,master,rows, columns):
        '''ConnectGrid(master)
        creates a new blank Connect 4 grid'''
        # set up listeners
        # initialize a new Frame
        Frame.__init__(self,bg='black') #makes a frame
        self.grid() #puts frame in grid
        self.columns = columns #number of columns
        self.rows = rows #number of rows
        self.redTurn = True
        # put in lines between the cells
        # (odd numbered rows and columns in the grid)
        # create the cells
        self.wins = []
        self.cells = {} # set up dictionary for cells
        self.labels = {}
        self.numTurns = 0
        for column in range(1, columns+1):
            for row in range(rows+1):
                coord = (column,row)
                if row == 0:
                    self.cells[coord] = Connect4Button(self,coord) #makes cells
                # cells go in even-numbered rows/columns of the grid
                    self.cells[coord].grid(row=row,column=column) #puts cells on grids
                else:
                    self.labels[coord] = Connect4Label(self,coord)
                    self.labels[coord].grid(row=row, column=column)
                    #Above part of this for loop taken from Intermediate Python AoPS course
                    if row >= 4:
                        self.wins.append([(column,row), (column,row-1), (column,row-2), (column,row-3)])                       
                    if column >= 4:
                        self.wins.append([(column,row), (column-1,row), (column-2,row), (column-3,row)])
                    if column >= 4 and row >= 4:
                        self.wins.append([(column,row), (column-1,row-1), (column-2,row-2), (column-3,row-3)])
                    if column >= 4 and row <= self.rows-3:
                        self.wins.append([(column,row), (column-1,row+1), (column-2,row+2), (column-3,row+3)])
        
    def play_turn(self, column):
        for row in range(self.rows,0,-1):
            coord = (column, row)
            if self.labels[coord].get_filled() == False:
                self.labels[coord].fill(self.redTurn)
                self.numTurns = 0
                self.check_win()
                return

    def change_turn(self):
        self.redTurn = not self.redTurn

    def check_win(self):
        for win in self.wins:
            if self.labels[win[0]].get_red_filled() == True and self.labels[win[1]].get_red_filled() == True and self.labels[win[2]].get_red_filled() == True and self.labels[win[3]].get_red_filled() == True:
                tkinter.messagebox.showinfo('Connect 4','Red wins!',parent=self) #This specific line taken from Intermediate Python AoPS course
            if self.labels[win[0]].get_yellow_filled() == True and self.labels[win[1]].get_yellow_filled() == True and self.labels[win[2]].get_yellow_filled() == True and self.labels[win[3]].get_yellow_filled() == True:
                tkinter.messagebox.showinfo('Connect 4','Yellow wins!',parent=self) #This specific line taken from Intermediate Python AoPS course
        if self.numTurns == self.rows * self.columns:
            tkinter.messagebox.showinfo('Connect 4','You tied',parent=self) #congradulations message
            

def connect4(rows, columns):
    '''connect4()
    plays Connect 4'''
    root = Tk()
    root.title('Connect 4')
    mg = ConnectGrid(root, rows, columns)
    root.mainloop()
    #Above connect4 function taken from Intermediate Python AoPS course
    
        

connect4(10,10)
