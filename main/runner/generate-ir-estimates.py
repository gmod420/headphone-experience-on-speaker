from main.dataHandler.StereoWavAudio import StereoWavAudio

def main():
   prepare_output()

def prepare_input():

    pass

def prepare_output():
    field_of_vision_stereo = StereoWavAudio(filePath="data/KGATLW/wavfile.wav")
    print(field_of_vision_stereo.audio_data)
    print(field_of_vision_stereo.sampleRate)
    # field_of_vision_stereo.
    pass
def generate_ir():
    pass

if __name__ == "__main__":
    main()

