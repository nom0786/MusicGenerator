# DATA533 - Project Doc
Noman Mohammad & Nyx Zhang
# Introduce
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

# Sub-Packages1 - Music Player
## Module1
Modele2

# Sub-Packages2 - Jam
## Module1 - FeatureSetting
- ### Class Introduction

```python
class FeatureSetting:
    def __init__(self, inputNotesList):
        return _
    def analyzer(self):
        return Result
    def key_generator(self):
        return key
    def rhythm_generator(self):
        return rhythm
```

The class name is **FeatureSetting**. It analyzes the input notes and sets the key and rhythm of the music.

- Store the input notes from the music player as initial.
- Analyze and Extract the features.
- Using based information to set key and rhythm.
- ### Functions
  - Function 1: analyzer
    - Using Empirical Probability and Music theory to analyze possible music features.
  - Function 2: key\_generator
    - Using the features to set the key of the music
  - Function 3: rhythm\_generator
    - Using the features to set the rhythm of the music

## Modele2 - Generator
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
