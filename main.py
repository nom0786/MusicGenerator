from MusicJam.music_generator import *

def main():
    tmp = MusicGenerator(note_object=[['C','G','B'],'1/2', 30],num_bars = 4,bpm=66)
    tmp.mix_melody_chords()

if __name__ == "__main__":
    main()
