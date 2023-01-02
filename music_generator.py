# imports
import os
from midi2audio import FluidSynth

class MusicGenerator:
    def __init__(self, model_path, sampling_rate, sound_font):
        self.model = model_path #load_model(model_path)
        self.sampling_rate = sampling_rate
        self.sound_font = sound_font


    def generate(self, seed_text, duration=100):
        
        return "test_output.mid"
    
    def convert_to_audio(self, midi_file_path):
        # call fluidsynth and pass midi to get wav file.
        # fluidsynth -ni soundfont.sf2 -F output.wav input.mid
        auio_path = str("music_gen/"+str(midi_file_path.split(".")[0]) + '.wav')
        FluidSynth(self.sound_font, self.sampling_rate).midi_to_audio(str("midi_gen/"+midi_file_path),auio_path)
        return auio_path