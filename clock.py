##tkinter is a package used to create graphical user interfaces
##which should be useful for creating a prototype for the smart mirror.
from tkinter import *
from tkinter.ttk import *


##retrieves systems time
from time import strtime

##creates the visual window
root = Tk()

root.title('Digital Clock')

##function strftime converts time objects to their string representation
def time(): 
  string = strftime('%H: %M: %S %p')
  label.config(text = string) 
  label.after(1000, time)
  
label = Label(root, font = ('Times New Roman', 60, 'bold'), background  = 'purple',
                         foreground = 'white')
                         
label.pack(anchor = 'center') 
time() 

mainloop()
