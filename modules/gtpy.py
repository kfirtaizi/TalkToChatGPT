import time

import pyttsx3
import pyttsx3.drivers

from modules.chrome import ChromeHandler
from modules.recorder import Recorder, play_waking_sound
import configparser


def start():
    config = configparser.ConfigParser()
    config.read('configuration/config.ini')

    ch = ChromeHandler()
    ch.launch_browser_by_profile(config['chrome']['profile_name'])
    wakeword = config['voice_input']['wakeword']

    recorder = Recorder()

    engine = pyttsx3.init()

    engine.setProperty('rate', int(config['voice_output']['rate']))
    engine.setProperty('volume', float(config['voice_output']['volume']))
    if config['voice_output']['gender'] == 'female':
        engine.setProperty('voice', engine.getProperty('voices')[1].id)

    while True:
        while True:
            audio = recorder.listen(stop_after_silence=0.2)
            if audio:
                if wakeword.lower() in audio.lower():
                    print("Wakeword detected! Starting recording...")
                    play_waking_sound()
                    break

        question = ''
        while question == '' or question is None:
            question = recorder.listen()

        ch.send_question(question)

        answer = ch.get_answer()
        while answer == ch.current_last_div or answer is None or answer == '':
            answer = ch.get_answer()

        time.sleep(0.5)  # Wait for the answer to load a little bit more
        answer = ch.get_answer()

        engine.startLoop(False)

        idx = 0
        while len(answer) > 0:
            engine.say(answer)
            engine.iterate()
            idx += len(answer)
            answer = ch.get_answer()[idx:]
        engine.endLoop()
