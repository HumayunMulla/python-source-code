# ComboBox Demo
import Tkinter
import Tkinter as tkinter
import ttk
import tkFont
from Tkinter import *
from ttk import *


# Get flyer name module
def foo(event):
    #print v.get()
    category = v.get()

# Main Root
root = Tkinter.Tk()
root.title("ComboBox Demo")

tab = ttk.Notebook(root)
tab1 = ttk.Frame(root)

tab.add(tab1, text = "ComboBox Demo")

tab.place(width=700, height=500)

labelframe = LabelFrame(tab1, text="Analyzer")
labelframe.pack(fill="both", expand="yes")

var = StringVar()
label1 = Label(labelframe, font="Tahoma 11", text="Select Flyer")
label1.place(x=10,y=18)



files = []
# here in this list you need to populate it with the data from MonoDB
options = ['','rcwhalen','JaJillian','smb50','vickie_risbie']
v = StringVar()#a string variable to hold user selection
#available combobox options

frame = Frame(labelframe)
frame.pack(side='top', fill='x', padx=12, pady=8)
#frame.place(x=125,y=10)
combo = Combobox(labelframe,textvariable=v, values=options,font="Tahoma 11")
combo.bind('<<ComboboxSelected>>',foo)#binding of user selection with a custom callback
combo.current(0)#set as default "option 2"
#combo.pack(side='left', anchor='w', padx=12, pady=8 )
combo.place(x=125,y=16)

root.resizable(width=FALSE, height=FALSE) # disable maximize button
root.geometry("700x500")
root.mainloop()
exit()
