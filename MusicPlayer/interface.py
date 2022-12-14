from tkinter import *
from tkinter import messagebox
import pygame
import time
from PIL import ImageTk, Image

from notes import *

#Global notes object 
n = notes()

class MusicInterface(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root
        self.initialize_interface()

    def initialize_interface(self):
        self.root.title('Music Player')
        self.root.geometry('725x350')
        self.root.configure(background='white')
        self.root.resizable(0,0)
        
        #set weights to main frame
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        
        #intialize mixer
        pygame.mixer.init()
        
        
        self.music_file = 'file.mid'
        color = "light gray"
        notes_disp = StringVar()
        
        #piano keys
        def value_C():
            notes_disp.set(n.addNote("C", time.time()))
            sound = pygame.mixer.Sound("notes/C.wav")
            sound.play()
            
        def value_D():
            notes_disp.set(n.addNote("D", time.time()))
            sound = pygame.mixer.Sound("notes/D.wav")
            sound.play()
            
        def value_E():
            notes_disp.set(n.addNote("E", time.time()))
            sound = pygame.mixer.Sound("notes/E.wav")
            sound.play()
            
        def value_F():
            notes_disp.set(n.addNote("F", time.time()))
            sound = pygame.mixer.Sound("notes/F.wav")
            sound.play()
            
        def value_G():
            notes_disp.set(n.addNote("G", time.time()))
            sound = pygame.mixer.Sound("notes/G.wav")
            sound.play()
            
        def value_A():
            notes_disp.set(n.addNote("A", time.time()))
            sound = pygame.mixer.Sound("notes/A.wav")
            sound.play()
            
        def value_B():
            notes_disp.set(n.addNote("B", time.time()))
            sound = pygame.mixer.Sound("notes/B.wav")
            sound.play()
            
        def popup():
            messagebox.showwarning("Warning!", "Cannot play. No music was generated!")
        
        def loadImage(image):
            image = PhotoImage(file=image)
            
        
            
            
        def generate():
#           jam = musicjam.MusicGenerator()
#           jam.generateMusic()

            self.music_file = 'test_file.mid'
            print(self.music_file)
            n.clearNotes()
            notes_disp.set("Done. Click play!")
            
    
        def play():
            if self.music_file != 'none':
                notes_disp.set("playing...")
                sound = pygame.mixer.Sound(self.music_file)
                sound.play()
                
            else:
                #in case user clicks notes then play... tell them that 
                print(self.music_file)
                notes_disp.set(" ")
                n.clearNotes()
                popup()

            

        main_frame = Frame(root, bg = color, bd = 20, relief = RIDGE)
        main_frame.grid()
        
        upper_frame = Frame(main_frame, bg = color, bd = 10, relief = RIDGE)
        upper_frame.grid(row = 0, column = 0)
        
        middle_frame = Frame(main_frame, bg = color, bd = 10, relief = FLAT)
        middle_frame.grid(row = 1, column = 0)
        
        lower_frame = Frame(main_frame, bg = color, bd = 10, relief = RIDGE)
        lower_frame.grid(row = 2, column = 0)
        
        
        Label(upper_frame, text="Piano Musical Keys", font=('arial', 25, 'bold'), padx=8, pady=8, bd=4, bg=color, fg = "white", justify=CENTER).grid(row=0, column=0, columnspan=11)
        
#         Label(middle_frame, text="INSERT IMAGE HERE", font=('arial', 25, 'bold'), padx=8, pady=8, bd=4, bg=color, fg = "white", justify=CENTER).grid(row=0, column=0, columnspan=11)
#         my_image = ImageTk.PhotoImage(Image.open("test_image.jpg"))
#         image_label = Label(middle_frame, image = my_image, font=('arial', 25, 'bold'), padx=8, pady=8, bd=4, bg=color, fg = "white", justify=CENTER).grid(row=0, column=0, columnspan=11

        
        play = Button(upper_frame, text="Play", font=('arial', 30, 'bold'), bd=5, bg=color, fg="black", justify=CENTER, command = play).grid(row=0, column=1,pady=1)
        note_display = Entry(upper_frame, textvariable = notes_disp, font=('arial', 25, 'bold'), bd=10, bg=color, fg = "white", justify=CENTER, state= "disabled").grid(row=0, column=2,pady=1)
        Generate = Button(upper_frame, text="Generate", font=('arial', 30, 'bold'), bd=5, bg=color, fg = "black", justify=CENTER, command = generate).grid(row=0, column=3,pady=1)
        
        btn_C = Button(lower_frame, bd = 4, width = 3, height = 7, text = "C", bg = "white", fg = "black", font = ('arial', 18, 'bold'), command = value_C)
        btn_C.grid(row = 0, column = 0, padx = 5, pady = 5)
        
        btn_D = Button(lower_frame, bd = 4, width = 3, height = 7, text = "D", bg = "white", fg = "black", font = ('arial', 18, 'bold'), command = value_D)
        btn_D.grid(row = 0, column = 1, padx = 5, pady = 5)

        btn_E = Button(lower_frame, bd = 4, width = 3, height = 7, text = "E", bg = "white", fg = "black", font = ('ariel', 18, 'bold'), command = value_E)
        btn_E.grid(row = 0, column = 2, padx = 5, pady = 5)

        btn_F = Button(lower_frame, bd = 4, width = 3, height = 7, text = "F", bg = "white", fg = "black", font = ('ariel', 18, 'bold'), command = value_F)
        btn_F.grid(row = 0, column = 3, padx = 5, pady = 5)

        btn_G = Button(lower_frame, bd = 4, width = 3, height = 7, text = "G", bg = "white", fg = "black", font = ('ariel', 18, 'bold'), command = value_G)
        btn_G.grid(row = 0, column = 4, padx = 5, pady = 5)

        btn_A = Button(lower_frame, bd = 4, width = 3, height = 7, text = "A", bg = "white", fg = "black", font = ('ariel', 18, 'bold'), command = value_A)
        btn_A.grid(row = 0, column = 5, padx = 5, pady = 5)

        btn_B = Button(lower_frame, bd = 4, width = 3, height = 7, text = "B", bg = "white", fg = "black", font = ('ariel', 18, 'bold'), command = value_B)
        btn_B.grid(row = 0, column = 6, padx = 5, pady = 5)
            
        
root = Tk()

player = MusicInterface(root)
root.mainloop()