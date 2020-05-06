""" The mian module of catsleep tool """

import os
import sys
import time
import json

sys.path.append('..')
from catsleep.utils import Utility
from catsleep.config import Config

DEBUG = False

class CatSleep():
    """ A class that represents the basic operation of catsleep """

    def __init__(self):
        """ Initialize all the basic attributes required for catsleep """
        if DEBUG:
            print(f'Initializing catsleep ...')
        self.util = Utility()
        if DEBUG:
            print('Cat Sleep is running.')


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

    
    def load_database(self):
        """ A method to load database files for audio, beep, texts from data.json file """
        database_path = "./catsleep/data.json"
        try:
            with open(database_path, 'r') as rf:
                data = json.load(rf)
            return data
        except FileNotFoundError:
            if DEBUG:
                print("Databse file not found.")
            return {}


    def catsleep_control(self):
        """ A method to control the interval and frequency of alarm """
        #Show a notification that catsleep is running and will send notification for break
        self.display_notification("Cat Sleep", "Cat Sleep is running and will send notification to take break.")

        #load the databse file for audio, text and beep sound
        data = self.load_database()
        if DEBUG:
            print(f'Databse files: {data}')

        while True:
            try:
                # try to get configurations
                conf = Config()
                configs = conf.get_user_config()

                #get selected audio, text and beep for this specifi notification
                audio_path, beep_path, text_message = self.util.select_beep_audio_text(data)
                if DEBUG:
                    print(f'audio path: {audio_path} - beep path: {beep_path} - text message: {text_message}')
                #wait for certain period before next alarm
                time.sleep(configs['interval'])

                for alarm in range(configs['frequency']):
                    #check if beep playing is set as true or not
                    #first play a beep sound, different beep at different time, need to make dynamic
                    if configs['play_beep'].lower() == "yes":
                        if beep_path is not None:
                            self.play_beep(beep_path)
                        else:
                            self.play_beep()
                    
                    #check if showing text is set as true or not
                    #then display the text notification, different text at different time, need to make dynamic
                    if configs['show_text'].lower() == "yes":
                        if text_message is not None:
                            self.display_notification("Take Break!", text_message)
                        else:
                            self.display_notification("Take Break!", "Hey, you should take a break")
                    
                    #check if playing audio message is set as true or not
                    #then play a voice message, different message at different time, need to make dynamic
                    if configs['play_audio'].lower() == "yes":
                        if audio_path is not None:
                            self.play_audio(audio_path)
                        else:
                            self.play_audio("./catsleep/audio/take_break_audio_1.wav")
                    time.sleep(configs['frequency_interval'])
            except Exception as e:
                self.util.show_text("Error!", "Something went wrong!")




if __name__ == '__main__':
    catsleep = CatSleep()
    catsleep.catsleep_control()