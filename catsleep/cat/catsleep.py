""" The mian module of catsleep tool """

import os
import sys
import time
import json
from pathlib import Path

from .utils import Utility
from .config import Config

DEBUG = True

class CatSleep():
    """ A class that represents the basic operation of catsleep """

    def __init__(self):
        """ Initialize all the basic attributes required for catsleep """
        if DEBUG:
            print('Initializing catsleep ...')
        self.util = Utility()
        self.conf = Config()
        if DEBUG:
            print('Cat Sleep is running.')
        self.default_audio_path = str(Path(__file__).parent / self.conf.path_to_default_notification_audio)


    def play_beep(self, beep_path):
        """ A method to play beep sound for catsleep """
        try:
            self.util.play_audio(beep_path)
        except FileNotFoundError:
            self.util.show_text("Error!", "Something went wrong with the beep notification!")


    def play_audio(self, audio_path):
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

    
    def load_database(self):
        """ A method to load database files for audio, beep, texts from data.json file """
        database_path = self.conf.db_path
        if DEBUG:
            print("database path: {}".format(database_path))
        try:
            with open(str(database_path), 'r') as rf:
                data = json.load(rf)
            return data
        except Exception as e:
            if DEBUG:
                print("Databse file not found. {}".format(e))
            return {}


    def catsleep_control(self):
        """ A method to control the interval and frequency of alarm """
        #Show a notification that catsleep is running and will send notification for break
        time.sleep(3)
        self.display_notification("Cat Sleep", "Cat Sleep is running and will send notification to take break.")

        #load the databse file for audio, text and beep sound
        data = self.load_database()
        if DEBUG:
            print("Databse files: {}".format(data))

        while True:
            try:
                # try to get configurations
                
                user_conf = self.conf.get_user_config()
                if DEBUG:
                    print('voice: {}'.format(user_conf["voice"]))

                #get selected audio, text and beep for this specifi notification
                audio_path, beep_path, text_message = self.util.select_beep_audio_text(data, user_conf['voice'])
                if DEBUG:
                    print('audio path: {} - beep path: {} - text message: {}'.format(audio_path, beep_path, text_message))
                #wait for certain period before next alarm
                time.sleep(user_conf['interval'])

                for alarm in range(user_conf['frequency']):
                    #check if beep playing is set as true or not
                    #first play a beep sound, different beep at different time, need to make dynamic
                    if user_conf['play_beep'].lower() == "yes":
                        if beep_path:
                            self.play_beep(beep_path)
                        else:
                            self.play_beep()
                    
                    #check if showing text is set as true or not
                    #then display the text notification, different text at different time, need to make dynamic
                    if user_conf['show_text'].lower() == "yes":
                        if text_message:
                            self.display_notification("Take Break!", text_message)
                        else:
                            self.display_notification("Take Break!", "Hey, you should take a break")
                    
                    #check if playing audio message is set as true or not
                    #then play a voice message, different message at different time, need to make dynamic
                    if user_conf['play_audio'].lower() == "yes":
                        if audio_path:
                            self.play_audio(audio_path)
                        else:
                            self.play_audio(self.default_audio_path)
                    time.sleep(user_conf['frequency_interval'])
            except Exception as e:
                self.util.show_text("Error!", "Something went wrong!")




if __name__ == '__main__':
    catsleep = CatSleep()
    catsleep.catsleep_control()