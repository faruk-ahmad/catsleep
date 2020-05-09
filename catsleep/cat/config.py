""" A module for setting and getting configurations of catsleep """

import json
import sys
import os
from os.path import expanduser
from pathlib import Path
import shutil

class Config():
    """ A class for maintaining configurations of catsleep """

    def __init__(self):
        """ Initialize all the attributes """
        self.cat_base_dir = Path(__file__).parent
        self.default_config_path = self.cat_base_dir / "../db/defaults.json"
        self.path_home = expanduser("~")
        self.user_config_path = os.path.join(self.path_home, '.catsleep_config.json')
        self.path_to_default_notification_audio = '../db/default_notification.ogg'
        self.db_path = self.cat_base_dir / "../db/data.json"

    def set_user_config(self, configs):
        """ A method for creating user configuration file """
        try:
            shutil.copyfile(self.default_config_path, self.user_config_path)
        except Exception as e:
            print('Error in writing user configurations.' + str(e))

    def get_user_config(self):
        """ A method to get user defined configurations """
        try:
            #built in open in python 3.5 does not support Pathlib like path, so to work in py 3.5 and 3.6 need to convert it into string
            with open(str(self.user_config_path), 'r') as urf:
                user_configs = json.load(urf)
            return user_configs
        except Exception as e:
            print('Error in loading user defined configuration. Loading default configurations.')
            return self.get_default_config()        

    def get_default_config(self):
        """ A method returning all the default configurations """
        try:
            with open(str(self.default_config_path), 'r') as drf:
                default_configs = json.load(drf)
                self.set_user_config(default_configs)
            return default_configs
        except Exception as e:
            print('Configuration error!' + str(e))
            return {}



if __name__ == '__main__':
    conf = Config()
    
    try:
        print('user configurations:')
        print(conf.get_user_config())
    except Exception as e:
        print('default configurations:')
        print(conf.get_default_config())