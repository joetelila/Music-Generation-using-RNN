#!/usr/bin/env python
# coding: utf-8

# # Hidden markov model generalized to 2 parenting relationship (also ngram model, n=3)

# In[1]:


# P(X_i|X_i-1,X_i-2)


# In[2]:


import nltk
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle 
import json
import os
from pathlib import Path
from IPython.display import Image, Audio
from music21 import note , chord , stream , instrument , converter   
import mido


# In[3]:


# create a dict with the ngram model, it receives a list with the samples as string
ngram_dict = {}

def create_trigram_dict(corpus):
    n = 3
    ngrams = nltk.ngrams(corpus, n)
    
    for grams in ngrams:
        dict_key = grams[:-1][0] + " " + grams[:-1][1]
        if dict_key in ngram_dict:
            ngram_dict[dict_key].append(grams[-1])
        else:
            ngram_dict[dict_key] = []
            ngram_dict[dict_key].append(grams[-1])


# In[4]:


def generate_trigram(seed, samples, ngram_dict):
    output = seed  
    for i in range(samples):
        # When it reaches the last prefix, there is no suffix, so end
        try:
            new_sample = random.choice(ngram_dict[seed])
        except:
            return output
        output += " " + new_sample
        seed = seed.split(" ")[1] + " " + new_sample

    return output


# In[5]:


songs = []
for filename in os.listdir("dataset/midi_songs"):
    if filename.endswith(".mid"): 
        #print(filename)
        s = 'dataset/midi_songs/'+filename
        #song = mido.MidiFile(s)
        conv = converter.parse(s)
        songs.append(conv)
        continue
    else:
        continue


# In[7]:


songs[0].show()


# In[8]:


notes = []
for s in songs:
    notes_to_parse = s.flat.notes
    notes.append(notes_to_parse)
    


# In[9]:


notes[:5]


# In[10]:


#                                      song1  song2
#generate list of list of notes --> [[A,F,C],[D,G,B]]
listoflists = []
for n in notes:
    notes_demo = []
    for element in n:
        # if the element is a Note , then store it's Pitch
        if isinstance(element , note.Note):
            notes_demo.append(str(element.pitch))
        
        elif isinstance(element , chord.Chord):
            notes_demo.append('+'.join(str(n) for n in element.normalOrder))
            
    listoflists.append(notes_demo)
        


# In[11]:


# converting into a single string each song in listoflists
final = []
for song in listoflists:
    l = song
    melody = ''
    for i in l:
        melody = melody + ' ' + i
    final.append(melody)
    melody = ''


# # Dictionaries has an ngram_dict in each position (for each song)

# In[12]:


dictionaries = []
for progression in final:
    ngram_dict = {}
    create_trigram_dict(progression.split(" "))
    dictionaries.append(ngram_dict)
    


# In[13]:


st = ''
l = dictionaries[5]
sample = 30
keys = list(l.keys()) # gets the key for producing a trigram
generated_melody = generate_trigram(keys[0], sample, l)
st = "tinyNotation: 3/4" + generated_melody


# In[14]:


littleMelody = converter.parse(st)
littleMelody.show('midi')


# In[15]:


littleMelody.show()


# In[ ]:




