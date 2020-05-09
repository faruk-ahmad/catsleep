""" A utility module that maintains the audio message and text message notification """

import os
import random
from pathlib import Path

DEBUG = True


class Utility():
    """ A class that holds the method for playing audio message and text message """
    def __init__(self):
        self.text_error_title = "Error Occured!"
        self.text_error_message = "Something wrong happened with the text notification!"
        self.path_home = Path(__file__).parent / "../"
        random.seed(22)

    def show_text(self, title, message):
        """ A method to display text message as system notification """
        
        try:
            os.system('notify-send "'+title+'" "'+message+'"')
        except Exception as e:
            os.system('notify-send "'+self.text_error_title+'" "'+self.text_error_message+'"')

    def play_audio(self, audio_path):
        """ A method to play audio as system notification """
        try:
            os.system('paplay ' + audio_path)
        except FileNotFoundError:
            self.show_text("Audio file not found!")


    def select_beep_audio_text(self, data, voice):
        """ A method to select a random beep, audio and respective text transcript of the selected audio """
        try:
            if DEBUG:
                print("data is: {}".format(data))
            messages = data['message']
            beep_data = data['beep']

            beep_index = random.randint(1, len(beep_data))

            beep_temp_path = 'beep_' + str(beep_index)
            #built in open does not support pathlib like path, need to convert in 
            #string for working in both python 3.5 and 3.6
            beep_path = os.path.join(str(self.path_home), beep_data[beep_temp_path])

            if voice.lower() != "male" and voice.lower() != "female":
                voice_id = random.randint(1, 2)
                if voice_id == 1:
                    voice = "male"
                elif voice_id == 2:
                    voice = "female"

            message = messages[voice]
            message_index = random.randint(1, len(message))
            audio_temp_path = message[str(message_index)]['audio']
            audio_path = os.path.join(str(self.path_home), audio_temp_path)
            text_message = message[str(message_index)]['text']

            return audio_path, beep_path, text_message
        except Exception as e:
            print("Following exception occured in sound file: {}".format(e))
            return None, None, None