import spacy
import string
from spacy.lang.pl import Polish




nlp = spacy.load("pl_core_news_md")


NAME = 'Ricardo'

class NaturalLanguageUnderstanding():
    def __init__(self, text):
        self.text = text
    def textToFrame():
        pass

class DialogueStateTracker():
    def __init__(self, frame):
        self.frame = frame
    def NLUFrameToDSTFrame():
        pass

class DialoguePolicy():
    def __init__(self, frame):
        self.frame = frame
    def DSTFrameToDPFrame():
        pass

class NaturalLanguageGeneration():
    def __init__(self, frame):
        self.frame = frame
    def DPFrameToText():
        pass

if __name__ == "__main__":

    print(f"Hello World. I am {NAME}")