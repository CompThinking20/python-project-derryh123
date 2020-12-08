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
    cal_gui = Tk()

    #background color
    cal_gui.config(background = "blue")

    cal_gui.title("Calendar")

    cal_gui.geometry("500x600")

    #returns text as string
    new_year = int(year_field.get())

    #method from calendar module which returns calendar of given year
    cal_content = calendar.calendar(new_year)

    cal_year = Label(cal_gui, text = cal_content, font = "Calibri 10 bold")

    cal_year.grid(row = 5, column = 1, padx = 20)

    cal_gui.mainloop()

##driver
if ___name__ ==  "__main__":

    gui = Tk()

    gui.config(background = "white")


    gui.title("CALENDER")

    ##tkinter window with dimensions 250x140
    gui.geometry("250x140")


    cal = Label(gui, text = "CALENDAR", bg = "dark gray",
                            font = ("times", 28, 'bold'))

    # where you enter the year
    year = Label(gui, text = "Enter Year", bg = "light green")

    # text entry box
    year_entry = Entry(gui)

    # Create a button to show calendar
    Display = Button(gui, text = "Show Calendar", fg = "Black",
                              bg = "Red", command = Calendar)

    Exit = Button(gui, text = "Exit", fg = "Black", bg = "Red", command = exit)

    # grid method is used for placing
    # components at certain positions
    cal.grid(row = 1, column = 1)

    year.grid(row = 2, column = 1)

    year_entry.grid(row = 3, column = 1)

    Display.grid(row = 4, column = 1)

    Exit.grid(row = 6, column = 1)

    ##starts the gui
    gui.mainloop()

        
