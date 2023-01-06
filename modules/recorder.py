import math
import os
import struct
import time

import pyaudio
import speech_recognition as sr
import warnings
import pyglet

Threshold = 5

SHORT_NORMALIZE = (1.0 / 32768.0)
chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
swidth = 2

TIMEOUT_LENGTH = 5


def play_waking_sound():
    warnings.filterwarnings("ignore", category=UserWarning, module='pyglet')

    player = pyglet.media.Player()
    waking_sound_mp3_path = os.path.join(os.getcwd(), r"assests\Google Now Voice.mp3")
    source = pyglet.media.load(waking_sound_mp3_path)
    player.queue(source)

    player.play()


class Recorder:

    @staticmethod
    def rms(frame):
        count = len(frame) / swidth
        format = "%dh" % (count)
        shorts = struct.unpack(format, frame)

        sum_squares = 0.0
        for sample in shorts:
            n = sample * SHORT_NORMALIZE
            sum_squares += n * n
        rms = math.pow(sum_squares / count, 0.5)

        return rms * 1000

    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=FORMAT,
                                  channels=CHANNELS,
                                  rate=RATE,
                                  input=True,
                                  output=True,
                                  frames_per_buffer=chunk)

    def record(self, stop_after_silence):
        print('Noise detected, recording beginning')
        rec = []
        current = time.time()
        end = time.time() + TIMEOUT_LENGTH
        silence_start = None  # variable to store the start time of silence

        while current <= end:
            data = self.stream.read(chunk)
            if self.rms(data) >= Threshold:
                end = time.time() + TIMEOUT_LENGTH
                silence_start = None  # reset the start time of silence
            else:
                # if it's the first sample of silence, store the start time
                if silence_start is None:
                    silence_start = time.time()
                # if it's been 5 second since the start of silence, stop the recording
                elif time.time() - silence_start >= stop_after_silence:
                    break

            current = time.time()
            rec.append(data)
        return self.convert_to_text(b''.join(rec))

    def convert_to_text(self, recording):
        r = sr.Recognizer()
        audio = sr.AudioData(recording, RATE, sample_width=self.p.get_sample_size(FORMAT))
        try:
            text = r.recognize_google(audio)
            # If the speech recognition was successful, print the recognized text
            return text
        except sr.UnknownValueError:
            # If the speech recognition failed, print an error message
            print("Unable to recognize speech.")
        except sr.RequestError as e:
            # If there was an error with the speech recognition service, print an error message
            print("Error with the speech recognition service: {0}".format(e))

    def listen(self, stop_after_silence=5):
        print('Listening beginning')
        while True:
            input = self.stream.read(chunk)
            rms_val = self.rms(input)
            if rms_val > Threshold:
                return self.record(stop_after_silence)
