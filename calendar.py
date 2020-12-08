import calendar 
from tkinter import *


##simple python program to display one month of the year 
#yy = 2020
#mm = 12

##print(calendar.month(yy, mm))


##This function for the calendar is a little more interactive.
##Its a gui and creates a separate window to view the date.
##this function shows the whole year as well 
##I wanted to test out something more interactive since 
##it will be part of a smart mirror which should include visual components.
def Calendar():
    
    #creates graphical interface window
    new_gui = Tk()

    #background color
    new_gui.config(background = "blue")

    new_gui.title("Calendar")

    new_gui.geometry("500x600")

    #returns text as string
    fetch_year = int(year_field.get())

    #method from calendar module which returns calendar of given year
    cal_content = calendar.calendar(fetch_year)

    cal_year = Label(new_gui, text = cal_content, font = "Calibri 10 bold")

    cal_year.grid(row = 5, column = 1, padx = 20)

    new_gui.mainloop()

##driver
if ___name__ ==  "__main__":

    gui = Tk()

    gui.config(background = "white") 
  
    
    gui.title("CALENDER") 
  
    
    gui.geometry("250x140") 
  
     
    cal = Label(gui, text = "CALENDAR", bg = "dark gray", 
                            font = ("times", 28, 'bold')) 
  
    # where you enter the year 
    year = Label(gui, text = "Enter Year", bg = "light green") 
      
    # text entry box  
    year_field = Entry(gui) 
  
    # Create a button to show calendar 
    Show = Button(gui, text = "Show Calendar", fg = "Black", 
                              bg = "Red", command = Calendar) 
  
    Exit = Button(gui, text = "Exit", fg = "Black", bg = "Red", command = exit) 
      
    # grid method is used for placing  
    # the widgets at respective positions  
    cal.grid(row = 1, column = 1) 
  
    year.grid(row = 2, column = 1) 
  
    year_field.grid(row = 3, column = 1) 
  
    Show.grid(row = 4, column = 1) 
  
    Exit.grid(row = 6, column = 1) 

    ##starts the gui
    gui.mainloop() 
        
