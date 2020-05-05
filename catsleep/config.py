""" A module for setting and getting configurations of catsleep """

import json
import sys
import os
from os.path import expanduser

sys.path.append('..')

class Config():
    """ A class for maintaining configurations of catsleep """

    def __init__(self):
        """ Initialize all the attributes """
        path_home = expanduser("~")
        self.default_config_path = './catsleep/defaults.json'
        self.user_config_path = os.path.join(path_home, 'catsleep_config.json')

    def set_user_config(self, configs):
        """ A method for creating user configuration file """
        try:
            with open(self.user_config_path, 'w') as uwf:
                json.dump(configs, uwf)
        except Exception as e:
            print('Error in writing user configurations.' + str(e))

    def get_user_config(self):
        """ A method to get user defined configurations """
        try:
            with open(self.user_config_path, 'r') as urf:
                user_configs = json.load(urf)
            return user_configs
        except Exception as e:
            print('Error in loading user defined configuration. Loading default configurations.')
            return self.get_default_config()        

    def get_default_config(self):
        """ A method returning all the default configurations """
        try:
            with open(self.default_config_path, 'r') as drf:
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