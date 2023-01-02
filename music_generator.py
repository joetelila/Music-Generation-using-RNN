# imports
import os
import numpy as np
import random
from midi2audio import FluidSynth
from music21 import note , chord , stream , instrument , converter   
import pickle
from tensorflow.keras.models import load_model

class MusicGenerator:
    def __init__(self, model_path, sampling_rate, sound_font):
        # load model
        print("Loading model...")
        self.model = load_model("models/music_generator_lstm_0149.h5")
        print("Model loaded")
        self.sampling_rate = sampling_rate
        self.sound_font = sound_font
        self.model_inputs = self.load_data("dataset/model_inputs")
        self.notes =  self.load_data("dataset/notes")
        self.int_to_note =  self.load_data("dataset/int_to_note")
        self.n_vocab = len(set(self.notes))
    def load_data(self, data_path):
        # load data from data_path
        with open(data_path , "rb") as file:
            load_data = pickle.load(file)
        return load_data


    def generate(self, seed_text, duration=100):
        
        print("seed_Text: ", seed_text)
        # pick a random sequence from the input as a starting point for the prediction
        # inital sequence/pattern
        seed_pattern = self.model_inputs[np.random.randint(0 , len(self.model_inputs)-1)]    # 100

        predicted_outputs = []

        # generate 500 notes
        for indx in range(duration):
            inp_seq = np.reshape(seed_pattern , (1, len(seed_pattern), 1))   # convert to desired input shape for model
            inp_seq = inp_seq/float(self.n_vocab)  # normalize
            
            prediction = self.model.predict(inp_seq) #self.model_inputs[np.random.randint(0 , len(self.model_inputs)-1)]#model.predict(inp_seq)
            pred_idx = np.argmax(prediction)
            pred_note = self.int_to_note[pred_idx]
            
            predicted_outputs.append(pred_note)
            
            # remove the first note of the sequence and insert the output of the previous iteration at the end of the sequence
            seed_pattern.append(pred_idx)
            seed_pattern = seed_pattern[1:]

        return self.convert_to_midi(predicted_outputs)
        
    def convert_to_midi(self, predicted_outputs):
        offset = 0 
        output_notes = []
        
        for pattern in predicted_outputs:
            # if the pattern is a chord, first split the string up into an array of notes
            if ('+' in pattern) or pattern.isdigit():
                notes_in_chord = pattern.split('+')
                
                # Then we loop through the string representation of each note and create a Note object for each of them
                notes_tmp = []
                for current_note in notes_in_chord:
                    new_note = note.Note(int(current_note))         
                    new_note.storedInstrument = instrument.Piano()
                    notes_tmp.append(new_note)
                    
                new_chord = chord.Chord(notes_tmp)   # create Chords from list of notes(strings of pitch names)
                new_chord.offset = offset
                output_notes.append(new_chord)
            
            # if pattern is a Note, create a Note object using string representation of the pitch contained in the predicted pattern
            else:
                new_note = note.Note(pattern)
                new_note.offset = offset
                new_note.storedInstrument = instrument.Piano()
                output_notes.append(new_note) 
                
            offset += random.choice([0.5,1,2])   # Duration


        midi_stream = stream.Stream(output_notes)
        midi_name = str(random.randint(0,1000000)) + "_song.mid"
        midi_stream.write('midi', fp="midi_gen/"+midi_name)
        return midi_name

    def convert_to_audio(self, midi_file_path):
        # call fluidsynth and pass midi to get wav file.
        # fluidsynth -ni soundfont.sf2 -F output.wav input.mid
        auio_path = str("music_gen/"+str(midi_file_path.split(".")[0]) + '.wav')
        FluidSynth(self.sound_font, self.sampling_rate).midi_to_audio(str("midi_gen/"+midi_file_path),auio_path)
        return auio_path