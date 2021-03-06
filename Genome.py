# -*- coding: utf-8 -*-
# verwaltet die Genomsequenz als String
from Observable import Observable

class Genome(Observable):
    sequence = ""

    def __init__(self, initial_sequence = ""):
        self.sequence = initial_sequence
    def setSequence(self, sequence):
        # "Hallo Welt"
        self.sequence = sequence
        self.setChanged()
    def getSequence(self):
        return self.sequence
    def getSequenceLength(self):
        return len(self.sequence)
