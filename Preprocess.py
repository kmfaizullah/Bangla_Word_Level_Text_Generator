import gzip
import gensim 
import logging
import pickle
import os
import json
import pandas as pd
from gensim.models import KeyedVectors
from gensim.models import Word2Vec

class Process:
    def __init__(self, data_directory,length):
        self.directory = data_directory
        self.length = length
        
    def clean(self,string):
    
        value=['़','ा','ि','ी','ु','ू', 'े','ै','ो','ौ','्','ঁ','ং','অ','আ','ই','ঈ','উ','ঊ','ঋ','ঌ','এ','ঐ','ও','ঔ',
              'ক','খ','গ','ঘ','ঙ','চ','ছ','জ','ঝ','ঞ','ট','ঠ','ড','ঢ','ণ','ত','থ','দ','ধ','ন','প','ফ','ব','ভ','ম','য',
              'র','ল','ৱ','ৰ','শ','ষ','হ', '়','া','ি','ী','ু','ূ','ূ','ৄ','ে','ৈ','ো','ৌ','্','ৎ','ৠ','ৡ','০','২','১',
              '৩','৪','৫','৬','৭','৮','৯',' ','স','য়']

        no_punct = ""
        for char in string:
            if char in value:
                no_punct = no_punct + char
        return no_punct

    def TextProcess(self):
        my_list=[]
        for p1,q1, file in os.walk(self.directory):
            for z in file:
                with open(self.directory+z,'rb') as f:
                    data = pickle.load(f)
                    p = self.clean(data)
                    my_list.append(p)
        data_new = ''.join(str(e) for e in my_list)
        return data_new.split()

    def create_seq(self):
        text=self.TextProcess()
        length = self.length
        sequences = list()
        for i in range(length, len(text)):
            # select sequence of tokens
            seq = text[i-length:i+1]
            # store
            sequences.append(seq)
        return sequences

    def encode_seq(self):
        seq=self.create_seq()
        chars = sorted(list(set(self.TextProcess())))
        mapping = dict((c, i) for i, c in enumerate(chars))
        sequences = list()
        for line in seq:
            # integer encode line
            encoded_seq = [mapping[char] for char in line]
            # store
            sequences.append(encoded_seq)
        return sequences,mapping



