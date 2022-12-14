# DATA533 - Project Doc
Noman Mohammad & Nyx Zhang

# Introduction
- ### Music Player - Noman
  - Users can randomly choose three notes of their choice 
  - The notes will be sent to the music generator to be parsed into playable music 
  - The user can then select play in order to play the music generated from their note selection 
- ### Jam - Nyx
  - Analyze the input three notes. 
  - Generate chords regression based on the analysis results.
  - Generate rhythm and beats. 
  - Generate a melody based on the three notes and chords.
  - Mix the results into an audio file with the metadata.

=======
# Sub-Packages1 - Music Player
## Module1 - Interface generation
The class name is MusicInterface. Its main purpose is to create the underlying GUI for our program. It inherits the Frame class from the tkinter library.
- ### Functions
  - Function 1: Init function
  	- Calls the initialize_interface function which is designed to create the widgets within our interface
  - Function 2:  initialize_interface
  	- This function will create all the widgets for our interface
  - Function 3 - 7 : value_C - value_B
  	- These functions act upon a piano key click. They call a function from out notes.py module and set values for our notes class
  - Function 8: generate
  	- Will act upon the generate button. Calls our MusicJam.py module to generate music based on user input from selected keys. Also calls our notes.py module to clear notes object upon 		   music generation and set status on the main label
  - Function 9: play
  	- Will act upon the play button and play the generated ‘mid’ file from our MusicJam.py module.  Also calls our notes.py module to clear notes object upon music generation and set status on the main label
  
## Module2 - Note generation
- ### Functions
The class name is Notes. Its main purpose is to parse the data coming from the user. This includes duration, speed and error checking for expected note count. - ### Functions
  - Function 1: Init function
  	- Sets empty lists for notes and time
  - Function 2:  getDuration
  	- This function will return a ratio of the elapsed time between note selection approximated to the nearest set value 
  - Function 3: addNote
  	- This function appends selected note to our initialized list along with time note was clicked so that calculation of speed and duration is possible
  - Function 4: getSpeed
  	- This function calculates and returns the total elapsed time from first to last note click 
  - Function 5: getNote
	- Returns list of notes for label update in Music player interface
  - Function 6: clearNotes
	- Clears the current attributes set for class from user input. Called when music is generated/played
  - Function 7: getData
	- Packages data in form accepted by MusicJam.py module to be parsed and turned into music. This returns a list of notes, speed and duration
	
# Sub-Packages2 - Jam
## Module1 - FeatureSetting
- ### Class Introduction

```python
class FeatureSetting:
    def __init__(self, inputNotesObject):
        return _
    def analyzer(self):
        return Result
    def key_generator(self):
        return key
    def rhythm_generator(self):
        return rhythm
```

The class name is **FeatureSetting**. It analyzes the input notes Object and sets the key and rhythm of the music.

- Store the input notes and the durationRatio from the music player as initial.
- Analyze and Extract the features.
- Using based information to set key and rhythm.
- ### Functions
  - Function 1: analyzer
    - Using Empirical Probability and Music theory to analyze possible music features.
  - Function 2: key\_generator
    - Using the features to set the key of the music
  - Function 3: rhythm\_generator
    - Using the features to set the rhythm of the music

## Module2 - Generator
- ### Class Introduction
```python
class Generator(FeatureSetting):
    def __init__(self, key, rhythm):
        return _
    def melody_generator(self):
        return melodyStream
    def chords_generator(self):
        return chordsStream
    def mix_melody_chords(self)
        return audio,metadata
```

The class name is **Generator**. It inherits the **FeatureSetting** class

- Set all the parent class features as initial.
- The primary model that generates the music.
- Output the music audio, music score picture, and other metadata to the music player.
- ### Functions
  - Function 1: analyzer

Using models to generate the melody, which is a stream of notes.

- Function 2: key\_generator
  - Using models and features from the parent class to generate a stream of chords.
- Function 3: rhythm\_generator
  - Mix the stream of notes and stream of chords. 
  - Mix the score of the music.
  - Return the chords, score, and other metadata.

```json
metadata_sample = 
{
   // beats per minute
   // default and flexible
   "bpm":111,
   //  the major or minor scale around which a piece of music revolves
   //  default and fixed
   "Key":"C",
   // rhythmic pattern constituted by the grouping of basic temporal units, called beats, into regular measures, or bars
   // default and fixed
   "meter":"4/4",
   // music genre: such as Blues, Jazz, Metal.
   // default and fixed
   "genre":"pop",
   // chords of music melody in this key
   // model generated the whole melody chords divided by the bars.
   "chords":[
      {
      	// chords
         "chords":[
            "C",
            "G",
            "Am",
            "B-"
         ],
         // Offset of the chord in the unit beat
         "chordRythm":[
            "1",
            "2",
            "3",
            "4"
         ]
      },
      {
         "chords":[
            "G",
            "A",
            "C",
            "D"
         ],
         "chordRythm":[
            "1",
            "2",
            "3",
            "4"
         ]
      }
   ],
   // notes of music melody in this key
   // user random input several notes, then model generated the whole melody notes divided by the bars.
   "notes":[
      {
      	// notes
         "notes":[
            "C",
            "E",
            "A",
            "G",
            "C",
            "D",
            "F",
            "D"
         ],
         // Offset of the notes in the unit beat
         "notesRythm":[
            "0.25",
            "0.25",
            "0.125",
            "0.75",
            "1",
            "0.25",
            "0.5",
            "1"
         ]
      },
      {
         "notes":[
            "G",
            "A",
            "F",
            "G",
            "C",
            "D",
            "G",
            "D"
         ],
         "notesRythm":[
            "0.75",
            "1",
            "0.5",
            "0.25",
            "0.5",
            "1",
            "0.5",
            "1"
         ]
      }
   ]
}


```
>>>>>>> main
