""" A utility module that maintains the audio message and text message notification """

import os

class Utility():
    """ A class that holds the method for playing audio message and text message """
    def __init__(self):
        self.text_error_title = "Error Occured!"
        self.text_error_message = "Something wrong happened with the text notification!"

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