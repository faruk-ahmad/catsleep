""" A utility module that maintains the audio message and text message notification """

import os
import random

class Utility():
    """ A class that holds the method for playing audio message and text message """
    def __init__(self):
        self.text_error_title = "Error Occured!"
        self.text_error_message = "Something wrong happened with the text notification!"
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


    def select_beep_audio_text(self, data):
        """ A method to select a random beep, audio and respective text transcript of the selected audio """
        try:
            audio_data = data['audio']
            beep_data = data['beep']
            text_data = data['texts']

            audio_index = random.randint(1, len(audio_data))
            text_index = audio_index
            beep_index = random.randint(1, len(beep_data))

            root_path = './catsleep'

            audio_temp_path = 'audio_' + str(audio_index)
            beep_temp_path = 'beep_' + str(beep_index)
            text_temp_path = 'text_' + str(text_index)

            audio_path = os.path.join(root_path, audio_data[audio_temp_path])
            beep_path = os.path.join(root_path, beep_data[beep_temp_path])
            text_message = text_data[text_temp_path]

            return audio_path, beep_path, text_message
        except Exception as e:
            return None, None, None