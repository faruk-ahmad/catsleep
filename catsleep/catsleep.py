""" The mian module of catsleep tool """

import os
import sys


class CatSleep():
    """ A class that represents the basic operation of catsleep """

    def __init__(self):
        """ Initialize all the basic attributes required for catsleep """
        print(f'Initializing catsleep ...')


    def play_beep(self):
        """ A method to play beep sound for catsleep """
        print(f'Playing beep ...')


    def play_audio(self):
        """ A method to play audio for catsleep """
        print(f'Playing audio ...')




if __name__ == '__main__':
    catsleep = CatSleep()
    catsleep.play_beep()
    catsleep.play_audio()