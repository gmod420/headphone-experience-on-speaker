import numpy as np
from scipy.io import wavfile
import scipy.io.resample_poly

class StaticInput:
    sampleRate = 0
    audio_data = None
    audio_data_L = None
    audio_data_R = None
    startFrame = 0
    endFrame = 0
    filePath = None

    def __init__(self, filePath):
        readFile()

    def readFile(self, filePath):
        self.sampleRate, self.audio_data = wavfile.read(path)
        self.audio_data_L = self.audio_data[0]
        self.audio_data_R = self.audio_data[1]

    def setStartFrame(self, frequency, timestamp):
        self.startFrame = timestamp * frequency

    def setEndFrame(self, frequency, timestamp):
        self.endFrame = timestamp * frequency

    def get_L_audioSegment(self):
        return self.audio_data_L[startFrame:endFrame]

    def get_R_audioSegment(self):
        return self.audio_data_R[startFrame:endFrame]

    def downSample(self, newFrequency):
        upRate = 1
        downRate = np.round(self.sampleRate/newFrequency)
        self.audio_data_L = scipy.io.resample_poly(self.audio_data_L, up=upRate, down=downRate)
        self.audio_data_L = scipy.io.resample_poly(self.audio_data_L, up=upRate, down=downRate)
        self.audio_data[0] = self.audio_data_L
        self.audio_data[1] = self.audio_data_R
