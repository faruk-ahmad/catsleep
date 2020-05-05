""" The mian module of catsleep tool """

import os
import sys
import time

sys.path.append('..')
from catsleep.utils import Utility


class CatSleep():
    """ A class that represents the basic operation of catsleep """

    def __init__(self):
        """ Initialize all the basic attributes required for catsleep """
        print(f'Initializing catsleep ...')
        self.util = Utility()


    def play_beep(self, beep_path='./catsleep/default_notification.ogg'):
        """ A method to play beep sound for catsleep """
        try:
            self.util.play_audio(beep_path)
        except FileNotFoundError:
            self.util.show_text("Error!", "Something went wrong with the beep notification!")


    def play_audio(self, audio_path='./catsleep/default_notification.ogg'):
        """ A method to play audio for catsleep """
        try:
            self.util.play_audio(audio_path)
        except FileNotFoundError:
            self.util.show_text("Error!", "Something went wrong with the audio notification!")


    def display_notification(self, text_title, text_message):
        """ A method to display the notification message """
        try:
            self.util.show_text(text_title, text_message)
        except Exception as e:
            self.util.show_text("Error!", "Something went wrong with the text notification!")

    
    def catsleep_control(self, time_interval, frequency, frequency_interval):
        """ A method to control the interval and frequency of alarm """
        while True:
            try:
                for alarm in range(frequency):
                    #first play a beep sound, different beep at different time, need to make dynamic
                    self.play_beep()
                    #then display the text notification, different text at different time, need to make dynamic
                    self.display_notification("Take Break!", "Hey! you should take a break.")
                    #then play a voice message, different message at different time, need to make dynamic
                    self.play_audio("./catsleep/audio/take_break_audio_1.wav")
                    time.sleep(frequency_interval)
            except Exception as e:
                self.util.show_text("Error!", "Something went wrong!")
            time.sleep(time_interval)




if __name__ == '__main__':
    catsleep = CatSleep()
    catsleep.catsleep_control(20, 3, 3)