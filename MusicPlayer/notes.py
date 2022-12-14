class notes:
    def __init__(self):
        self.notes = []
        self.times = []
        
    def getDuration(self, times):
        #set duration times we will round to
        durations = [0.5, 1, 2]
        
        note12_dur = (times[1] - times[0])
        note23_dur = (times[2] - times[1])
        duration = (note12_dur/note23_dur)
        
        #rounding values to 1 of 3 durations set in list -> durations = [0.5, 1, 2]
        return min(durations, key = lambda x:abs(x-duration))
        
    def getSpeed(self, times):
        speed = (times[2] - times[0])
        return round(speed, 2)
    
    def addNote(self, note, time):
        if len(self.notes) != 3:
            self.notes.append(note)
            self.times.append(time)
            return self.notes
        else:
            return self.notes
        
    def getNotes(self):
        return self.notes
        
            
    #takes in the display note argument aswell (for the note display section) and set it to the emptied notelist when reset (generate)
    def clearNotes(self):
        self.notes.clear()
        self.times.clear()
        
    def getData(self):
        duration = self.getDuration(self.times)
        speed = self.getSpeed(self.times)
        return [self.notes, duration, speed]
