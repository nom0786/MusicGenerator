from tkinter import *
from tkinter import messagebox
from threading import Timer
import pygame
import time

from MusicPlayer.notes import *
from MusicJam.music_generator import *

#Global objects
n = notes()

class MusicInterface(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root
        self.initialize_interface(self.root)

    def check_notes(notes):
        if (len(notes) == 3):
            return True
        else:
            return False

    def initialize_interface(self, root):
        self.root.title('Music Player')
        self.root.geometry('720x350')
        self.root.configure(background='white')
        
        #set weights to main frame
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        #intialize mixer
        pygame.mixer.init()
        
        #intitially set the music file to none, generate() will update file. Might have to use global command in function
        self.music_file = 'none'
        self.playing_state = False
        
        #for the scheduled task. scheduled task will always run, but function depends on is_clicked condition
        self.is_clicked = True
        color = "light gray"
        notes_disp = StringVar()
        
        #piano keys
        def value_C():
            self.is_clicked = True
            check_sound()
            notes_disp.set(n.generate_note("C", time.time()))
            sound = pygame.mixer.Sound("MusicPlayer/notes/C.wav")
            sound.play()
            
        def value_D():
            self.is_clicked = True
            check_sound()           
            notes_disp.set(n.generate_note("D", time.time()))
            sound = pygame.mixer.Sound("MusicPlayer/notes/D.wav")
            sound.play()
            
        def value_E():
            self.is_clicked = True
            check_sound()
            notes_disp.set(n.generate_note("E", time.time()))
            sound = pygame.mixer.Sound("MusicPlayer/notes/E.wav")
            sound.play()
            
        def value_F():
            self.is_clicked = True
            check_sound()
            notes_disp.set(n.generate_note("F", time.time()))
            sound = pygame.mixer.Sound("MusicPlayer/notes/F.wav")
            sound.play()
            
        def value_G():
            self.is_clicked = True
            check_sound()
            notes_disp.set(n.generate_note("G", time.time()))
            sound = pygame.mixer.Sound("MusicPlayer/notes/G.wav")
            sound.play()
            
        def value_A():
            self.is_clicked = True
            check_sound()
            notes_disp.set(n.generate_note("A", time.time()))
            sound = pygame.mixer.Sound("MusicPlayer/notes/A.wav")
            sound.play()
            
        def value_B():
            self.is_clicked = True
            check_sound()
            notes_disp.set(n.generate_note("B", time.time()))
            sound = pygame.mixer.Sound("MusicPlayer/notes/B.wav")
            sound.play()

        def scheduled_task():
            if self.is_clicked:
                self.is_clicked = False
                return None
            else:
                notes_disp.set(" ")
                n.clear_notes()

        def run_scheduled_task():
            notes_disp.set("playing...")
            timer = Timer(14, scheduled_task)
            timer.start()
            
        def popup(msg):
            messagebox.showwarning("Warning!", msg)

        def check_notes_status(notes):
            if (len(notes) == 3):
                return True
            else:
                return False

        #chck whether music is playing
        def  check_sound():
            if self.playing_state == True:
                pygame.mixer.music.stop()
             
        def generate():
            try:
                #checking to see whether or not 3 notes were selected before user can proceed to music generation
                if (check_notes_status(n.get_notes())):
        
                    #generate the music by passing the user selected notes to MusicGenerator function
                    tmp = MusicGenerator(n.export_notes(),num_bars = 4,bpm=66)
                    tmp.mix_melody_chords()[0]

                    self.music_file = 'file.mid'
                    n.clear_notes()
                    notes_disp.set("Done. Click play!")
                    self.generate_status = True
                else:
                    popup("Cannot generate! Select a total of 3 keys.")
                    
            except Exception as err:
                print(f"Unexpected {err=}, {type(err)=}")
                raise

        def play():
            try:
                if self.music_file != 'none':
                    pygame.mixer.music.load(self.music_file)
                    pygame.mixer.music.play()
                    self.playing_state = True

                    #doesnt get called if file crashes as this part of code is never reached
                    self.music_file = 'none'
                    run_scheduled_task()   
                else:
                    popup("Cannot play! No music was generated.")

            except Exception as err:
                print(f"Unexpected {err=}, {type(err)=}")
                self.music_file = 'none'
                run_scheduled_task() 
                raise

        main_frame = Frame(root, bg = color, bd = 20, relief = RIDGE)
        main_frame.grid()
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)  

        upper_frame = Frame(main_frame, bg = color, bd = 10, relief = RIDGE)
        upper_frame.grid(row = 0, column = 0)
        upper_frame.columnconfigure(0, weight=1)
        upper_frame.columnconfigure(1, weight=1)
        upper_frame.columnconfigure(2, weight=1)
        upper_frame.columnconfigure(3, weight=1)
        upper_frame.rowconfigure(0, weight=1)
        
        lower_frame = Frame(main_frame, bg = color, bd = 10, relief = RIDGE)
        lower_frame.grid(row = 1, column = 0)
        lower_frame.columnconfigure(0, weight=1)
        lower_frame.columnconfigure(1, weight=1)
        lower_frame.columnconfigure(2, weight=1)
        lower_frame.columnconfigure(3, weight=1)
        lower_frame.columnconfigure(4, weight=1)
        lower_frame.columnconfigure(5, weight=1)
        lower_frame.columnconfigure(6, weight=1)
        lower_frame.rowconfigure(0, weight=1)  
        
        Label(upper_frame, text="Piano Musical Keys", font=('arial', 25, 'bold'), padx=8, pady=8, bd=4, bg=color, fg = "white", justify=CENTER).grid(row=0, column=0, columnspan=11)

        play = Button(upper_frame, text="Play", font=('arial', 30, 'bold'), bd=5, bg=color, fg="black", justify=CENTER, command = play).grid(row=0, column=1,pady=1)
        Entry(upper_frame, textvariable = notes_disp, font=('arial', 30, 'bold'), bd=10, bg=color, fg = "white", justify=CENTER, state= "disabled").grid(row=0, column=2,pady=1)
        generate = Button(upper_frame, text="Generate", font=('arial', 30, 'bold'), bd=5, bg=color, fg = "black", justify=CENTER, command = generate).grid(row=0, column=3,pady=1)
        
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


def run_interface():
    root = Tk()
    MusicInterface(root)
    root.mainloop()
    