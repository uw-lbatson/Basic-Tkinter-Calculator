#import tkinter for GUI
from tkinter import *

#define function calc
#returns source as frame pushed on side
def calc(source, side):
    store = Frame(source)
    store.pack(side=side, fill=BOTH)
    return store

#define function button
#returns source as a button with given text and command
def button(source, side, text, command=None):
    store = Button(source, text=text, command=command)
    store.pack(side=side, expand=YES, fill=BOTH)
    return store

class app(Frame):
    #define init function to run when app is initialized
    def __init__(self):
        #initialize tkinter frame
        Frame.__init__(self)
        #create text font
        self.option_add('*Font', 'arial 26 bold')
        #frame expands over any excess area
        self.pack(expand=YES, fill=BOTH)
        #create application name
        self.master.title('Calculator')

        #create display text using tkinter stringvar
        display = StringVar()
        
        #use entry widget to accept single line text str
        #textvariable defined as stringvar, pushed right,
        #border of 30px, packed on top, and fills extra space
        Entry(self, textvariable=display
                            , justify='right'
                                , bd=30).pack(side=TOP,
                                    expand=YES, fill=BOTH)

        #adds button C to clear display
        #when button is clicked, sets display to empty
        for clear in (["C"]):
            erase = calc(self, TOP)
            for char in clear:
                button(erase, LEFT, char,
                       lambda store=display, q=char:
                           store.set(''))

        #adds buttons for numbers and functions in rows
        #when any button is clicked, adds that number
        #or function to the display
        for nums in ("789/", "456*", "123-", "0.+"):
            func = calc(self, TOP)
            for equals in nums:
                button(func, LEFT, equals,
                       lambda store=display, q=equals:
                           store.set(store.get() + q))

        #adds button for equals sign
        #when button is clicked, uses class function
        # 'calc' on display to evaluate display
        equalsBtn = calc(self, TOP)
        for equals in "=":
            if equals == '=':
                btn = button(equalsBtn, LEFT, equals)
                btn.bind('<ButtonRelease-1>',
                         lambda e,s=self, store=display:
                             s.calc(store), '+')

    #define function calc in app class
    #attempts to evaluate display
    #otherwise, changes display to ERR
    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERR")
            
#run main function 'app' until closed
if __name__=='__main__':
    app().mainloop()
