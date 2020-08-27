#!/usr/bin/env python3
# V2.0X
# Local
import logger


import tkinter 
import os     
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import webbrowser

class PyPad: 
  
    __root = Tk() 
  
    # default window width and height 
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root) 
    __thisMenuBar = Menu(__root) 
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0) 
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0) 
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0) 
      
    # To add scrollbar 
    __thisScrollBar = Scrollbar(__thisTextArea)      
    __file = None
  
    def __init__(self,**kwargs): 
        
        # Set icon
        try:
            icon = PhotoImage(master=PyPad.__root, file='PyPad.png')
            PyPad.__root.wm_iconphoto(True, icon)
        except: 
                pass
  
        # Set window size (the default is 300x300) 
  
        try: 
            self.__thisWidth = kwargs['width'] 
        except KeyError: 
            pass
  
        try: 
            self.__thisHeight = kwargs['height'] 
        except KeyError: 
            pass
  
        # Set the window text 
        self.__root.title("Untitled - PyPad") 
  
        # Center the window 
        screenWidth = self.__root.winfo_screenwidth() 
        screenHeight = self.__root.winfo_screenheight() 
      
        # For left-alling 
        left = (screenWidth / 2) - (self.__thisWidth / 2)  
          
        # For right-allign 
        top = (screenHeight / 2) - (self.__thisHeight /2)  
          
        # For top and bottom 
        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, 
                                              self.__thisHeight, 
                                              left, top))  
  
        # To make the textarea auto resizable 
        self.__root.grid_rowconfigure(0, weight=1) 
        self.__root.grid_columnconfigure(0, weight=1) 
  
        # Add controls (widget) 
        self.__thisTextArea.grid(sticky = N + E + S + W) 
          
        # To open new file 
        self.__thisFileMenu.add_command(label="New [ctrl+n]", 
                                        command=self.__newFile)     
          
        # To open a already existing file 
        self.__thisFileMenu.add_command(label="Open [ctrl+o]", 
                                        command=self.__openFile) 
          
        # To save current file 
        self.__thisFileMenu.add_command(label="Save [ctrl+s]", 
                                        command=self.__saveFile)     
  
        # To create a line in the dialog         
        self.__thisFileMenu.add_separator()                                          
        self.__thisFileMenu.add_command(label="Exit [ctrl+d]", 
                                        command=self.__quitApplication) 
        self.__thisMenuBar.add_cascade(label="File", 
                                       menu=self.__thisFileMenu)      
          
        # To give a feature of cut  
        self.__thisEditMenu.add_command(label="Cut [ctrl+x]", 
                                        command=self.__cut)              
      
        # to give a feature of copy     
        self.__thisEditMenu.add_command(label="Copy [ctrl+c]", 
                                        command=self.__copy)          
          
        # To give a feature of paste 
        self.__thisEditMenu.add_command(label="Paste [ctrl+v]", 
                                        command=self.__paste)          
        self.__thisEditMenu.add_command(label="Search with Google",
                                        command=self.__search)  
        # To give a feature of editing 
        self.__thisMenuBar.add_cascade(label="Edit", 
                                       menu=self.__thisEditMenu)      
          
        # To create a feature of description of the notepad 
        self.__thisHelpMenu.add_command(label="About PyPad", 
                                        command=self.__showAbout)  
        self.__thisMenuBar.add_cascade(label="Help", 
                                       menu=self.__thisHelpMenu) 
  
        self.__root.config(menu=self.__thisMenuBar) 
  
        self.__thisScrollBar.pack(side=RIGHT,fill=Y)                     
          
        # Scrollbar will adjust automatically according to the content         
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

        # key bindings
        self.__root.bind("<Control-s>", self.__saveFile)
        self.__root.bind("<Control-c>", self.__copy)
        self.__root.bind("<Control-v>", self.__paste)
        self.__root.bind("<Control-x>", self.__cut)
        self.__root.bind("<Control-o>", self.__openFile)
        self.__root.bind("<Control-d>", self.__quitApplication)
        self.__root.bind("<Control-n>", self.__newFile)
        
      
          
    def __quitApplication(self, evt=None):
        #if self.__file = None
        if self.__file == None and not self.__thisTextArea.get(1.0, END).isspace():
            result = askyesnocancel("PyPad", "Do you want to save changes to Untitled?")
            if result:
                self.__saveFile()
                self.__root.destroy()
            elif result == False:
                self.__root.destroy()
            elif result == None:
                pass
        # exit() 
  
    def __showAbout(self): 
        showinfo("PyPad","A Lightweight Notepad written purely in Python 3.x.\n(c) 2020 Samuel Cheng") 
  
    def __openFile(self, evt=None): 
          
        self.__file = askopenfilename(defaultextension=".txt", 
                                      filetypes=[("All Files","*.*"), 
                                        ("Text Documents","*.txt")]) 
  
        if self.__file == "": 
              
            # no file to open 
            self.__file = None
        else: 
              
            # Try to open the file 
            # set the window title 
            self.__root.title(os.path.basename(self.__file) + " - PyPad") 
            self.__thisTextArea.delete(1.0,END) 
  
            file = open(self.__file,"r") 
  
            self.__thisTextArea.insert(1.0,file.read()) 
  
            file.close() 
  
          
    def __newFile(self, evt=None):
        if self.__file != None:
            self.__saveFile()
        logger.log(self.__file)
        self.__root.title("Untitled - PyPad") 
        self.__file = None
        self.__thisTextArea.delete(1.0,END) 
  
    def __saveFile(self, evt=None): 
  
        if self.__file == None: 
            # Save as new file 
            self.__file = asksaveasfilename(initialfile='Untitled.txt', 
                                            defaultextension=".txt", 
                                            filetypes=[("All Files","*.*"), 
                                                ("Text Documents","*.txt")]) 
  
            if self.__file == "": 
                self.__file = None
            else: 
                  
                # Try to save the file 
                file = open(self.__file,"w") 
                file.write(self.__thisTextArea.get(1.0,END)) 
                file.close() 
                  
                # Change the window title 
                self.__root.title(os.path.basename(self.__file) + " - Notepad") 
                  
              
        else: 
            file = open(self.__file,"w") 
            file.write(self.__thisTextArea.get(1.0,END)) 
            file.close() 
        logger.log("Saved!")  
    def __cut(self, evt=None): 
        self.__thisTextArea.event_generate("<<Cut>>") 
  
    def __copy(self, evt=None): 
        self.__thisTextArea.event_generate("<<Copy>>") 
  
    def __paste(self, evt=None): 
        self.__thisTextArea.event_generate("<<Paste>>")
    
    def __search(self, evt=None):
        try:
            content = self.__thisTextArea.selection_get()
            webbrowser.open("https://www.google.com/search?q={}".format(content))
        except:
            logger.log("Nothing selected!")


        
    def run(self): 
  
        # Run main application
        self.__root.protocol("WM_DELETE_WINDOW", self.__quitApplication)
        self.__root.mainloop()
        



if __name__ == "__main__":
    import platform
    if int(platform.python_version()[0]) < 3:
        raise Exception("Please use Python 3 or higher.", "python_version: {}".format(platform.python_version()))
    try:
        # Run main application 
        PyPad = PyPad(width=600,height=400) 
        PyPad.run()
    except Exception as e:
        logger.critical("Unkown Error Occurred:\n{}".format(e))
    
