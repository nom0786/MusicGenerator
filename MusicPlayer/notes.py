class notes:
    def __init__(self):
        self.notes = []
        self.times = []
        
    def get_notes(self):
        return self.notes
        
    def calculate_duration(self, times):
        #specified duration times the calcuated time will round to
        durations = [0.5, 1, 2]
        
        note12_dur = (times[1] - times[0])
        note23_dur = (times[2] - times[1])
        duration = (note12_dur/note23_dur)
        
        #rounding values to 1 of 3 durations set in list -> durations = [0.5, 1, 2]
        return min(durations, key = lambda x:abs(x-duration))
        
    def calculate_speed(self, times):
        speed = (times[2] - times[0])
        return round(speed, 2)
    
    def generate_note(self, note, time):
        if len(self.notes) != 3:
            self.notes.append(note)
            self.times.append(time)
            return self.notes
        else:
            return self.notes

    #convert number value to associated fraction
    def convert_duration(self, duration):
        if duration == 1:
            return '1/1'
        elif duration == 0.5:
            return '1/2'
        else:
            return '2/1'
            
    def clear_notes(self):
        self.notes.clear()
        self.times.clear()
        
    def export_notes(self):
        notes = self.notes
        duration = self.convert_duration(self.calculate_duration(self.times))
        speed = self.calculate_speed(self.times)
        return [notes, duration, speed]

