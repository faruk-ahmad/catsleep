""" The mian module of catsleep tool """

import os
import sys
import time
import json
import logging
from pathlib import Path

from .utils import Utility
from .config import Config

logging.basicConfig(
    format='%(asctime)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
    level=logging.INFO)


class CatSleep():
    """ A class that represents the basic operation of catsleep """

    def __init__(self):
        """ Initialize all the basic attributes required for catsleep """
        logging.info('Initializing catsleep ...')
        self.util = Utility()
        self.conf = Config()
        logging.info('Cat Sleep is running ...')
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
        logging.debug("database path: {}".format(database_path))
        try:
            with open(str(database_path), 'r') as rf:
                data = json.load(rf)
            return data
        except Exception as e:
            logging.error("Databse file not found.", exc_info=True)
            return {}


    def catsleep_control(self):
        """ A method to control the interval and frequency of alarm """
        #Show a notification that catsleep is running and will send notification for break
        time.sleep(10)
        self.display_notification("Cat Sleep", "Cat Sleep is running and will send notification to take break.")

        #load the databse file for audio, text and beep sound
        data = self.load_database()
        logging.debug("Databse files: {}".format(data))

        while True:
            try:
                # try to get configurations
                
                user_conf = self.conf.get_user_config()
                logging.debug('voice: {}'.format(user_conf["voice_mode"]))

                #get selected audio, text and beep for this specifi notification
                audio_path, beep_path, text_message = self.util.select_beep_audio_text(data, user_conf['voice_mode'])
                logging.info('audio path: {}'.format(audio_path))
                logging.info('beep path: {}'.format(beep_path))
                logging.info('text message: `{}`'.format(text_message))

                #wait for certain period before next alarm
                #user input is in minutes, need to convert in seconds
                sleep_time = user_conf['interval_minutes'] * 60
                logging.info('going sleep for {} sec ...'.format(sleep_time))
                time.sleep(sleep_time)

                for alarm in range(user_conf['frequency_number']):
                    #check if beep playing is set as true or not
                    #first play a beep sound, different beep at different time, need to make dynamic
                    if user_conf['play_beep_on'].lower() == "yes":
                        if beep_path:
                            self.play_beep(beep_path)
                        else:
                            self.play_beep()
                    
                    #check if showing text is set as true or not
                    #then display the text notification, different text at different time, need to make dynamic
                    if user_conf['show_text_on'].lower() == "yes":
                        if text_message:
                            self.display_notification("Take Break!", text_message)
                        else:
                            self.display_notification("Take Break!", "Hey, you should take a break")
                    
                    #check if playing audio message is set as true or not
                    #then play a voice message, different message at different time, need to make dynamic
                    if user_conf['play_audio_on'].lower() == "yes":
                        if audio_path:
                            self.play_audio(audio_path)
                        else:
                            self.play_audio(self.default_audio_path)
                    
                    #gap between two consecutive alarms at a slot
                    #user input is in minutes, need to convert in seconds
                    print('-' * 45)
                    time.sleep(user_conf['frequency_interval_minutes'] * 60)
            except Exception as e:
                print(e)
                self.util.show_text("Error!", "Something went wrong!")
