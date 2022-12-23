class DurationException(Exception):
    pass

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

        try:
            duration = (note12_dur/note23_dur)
        except ZeroDivisionError:
            print("divide by zero", ZeroDivisionError)
        
        #rounding values to 1 of 3 durations set in list -> durations = [0.5, 1, 2]
        return min(durations, key = lambda x:abs(x-duration))
        
    def calculate_speed(self, times):
        try:
            speed = (times[2] - times[0])
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise

        return round(speed, 2)
    
    def generate_note(self, note, time):
        try:    
            if len(self.notes) != 3:
                self.notes.append(note)
                self.times.append(time)
                return self.notes
            else:
                return self.notes
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise        

    #convert number value to associated fraction
    def convert_duration(self, duration):
        try: 
            if duration == 1:
                return '1/1'
            elif duration == 0.5:
                return '1/2'
            else:
                return '2/1'
        except:
            raise DurationException("incorrect duration amount")
            
    def clear_notes(self):
        self.notes.clear()
        self.times.clear()
        
    def export_notes(self):
        notes = self.notes
        duration = self.convert_duration(self.calculate_duration(self.times))
        speed = self.calculate_speed(self.times)
        return [notes, duration, speed]