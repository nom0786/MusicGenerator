#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
import pygame

class MusicInterface(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root
        self.initialize_interface()
        pygame.mixer.init()

    def initialize_interface(self):
        self.root.title('Music Player')
        self.root.geometry('725x415')
        self.root.configure(background='white')
        self.root.resizable(0,0)
        
        notes_disp = StringVar()
        color = "light gray"
        
        #will need an object to set the values in a list
        
        #test functions
        def value_C():
            notes_disp.set(notes_disp.get()+"C")
            
            
        def value_D():
            notes_disp.set("D")            
        
        
        main_frame = Frame(root, bg = color, bd = 10, relief = RIDGE)
        main_frame.grid()
        
        upper_frame = Frame(main_frame, bg = color, bd = 10, relief = RIDGE)
        upper_frame.grid(row = 0, column = 0)
        
        middle_frame = Frame(main_frame, bg = color, bd = 10, relief = RIDGE)
        middle_frame.grid(row = 1, column = 0)
        
        lower_frame = Frame(main_frame, bg = color, bd = 10, relief = RIDGE)
        lower_frame.grid(row = 2, column = 0)
        
        Label(upper_frame, text="Piano Musical Keys", font=('arial', 25, 'bold'), padx=8, pady=8, bd=4, bg=color, fg = "white", justify=CENTER).grid(row=0, column=0, columnspan=11)
        Label(middle_frame, text="INSERT IMAGE HERE", font=('arial', 25, 'bold'), padx=8, pady=8, bd=4, bg=color, fg = "white", justify=CENTER).grid(row=0, column=0, columnspan=11)
        
        play = Button(upper_frame, text="Play", font=('arial', 25, 'bold'), bd=10, bg=color, fg="white", justify=CENTER).grid(row=0, column=1,pady=1)
        note_display = Entry(upper_frame, textvariable = notes_disp, font=('arial', 25, 'bold'), bd=10, bg=color, fg = "white", justify=CENTER, state= "disabled").grid(row=0, column=2,pady=1)
        Generate = Button(upper_frame, text="Generate", font=('arial', 25, 'bold'), bd=10, bg=color, fg = "white", justify=CENTER).grid(row=0, column=3,pady=1)
        
        btn_C = Button(lower_frame, bd = 4, width = 3, height = 5, text = "C", bg = "white", fg = "black", font = ('arial', 18, 'bold'), command = value_C)
        btn_C.grid(row = 0, column = 0, padx = 5, pady = 5)
        
        btn_D = Button(lower_frame, bd = 4, width = 3, height = 5, text = "D", bg = "white", fg = "black", font = ('arial', 18, 'bold'), command = value_D)
        btn_D.grid(row = 0, column = 1, padx = 5, pady = 5)

        btn_E = Button(lower_frame, bd = 4, width = 3, height = 5, text = "E", bg = "white", fg = "black", font = ('ariel', 18, 'bold'))
        btn_E.grid(row = 0, column = 2, padx = 5, pady = 5)

        btn_F = Button(lower_frame, bd = 4, width = 3, height = 5, text = "F", bg = "white", fg = "black", font = ('ariel', 18, 'bold'))
        btn_F.grid(row = 0, column = 3, padx = 5, pady = 5)

        btn_G = Button(lower_frame, bd = 4, width = 3, height = 5, text = "G", bg = "white", fg = "black", font = ('ariel', 18, 'bold'))
        btn_G.grid(row = 0, column = 4, padx = 5, pady = 5)

        btn_A = Button(lower_frame, bd = 4, width = 3, height = 5, text = "A", bg = "white", fg = "black", font = ('ariel', 18, 'bold'))
        btn_A.grid(row = 0, column = 5, padx = 5, pady = 5)

        btn_B = Button(lower_frame, bd = 4, width = 3, height = 5, text = "B", bg = "white", fg = "black", font = ('ariel', 18, 'bold'))
        btn_B.grid(row = 0, column = 6, padx = 5, pady = 5)
            
        
root = Tk()
player = MusicInterface(root)
root.mainloop()

