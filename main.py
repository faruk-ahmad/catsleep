""" Main module to start the catsleep tool """

import os
import sys

#sys.path.append('./')
from catsleep.catsleep import CatSleep

def start_catsleep():
    """ Starting point of catsleep """
    time_interval = 30 #continuous alarm after this interval in seconds - integer
    frequency = 1 #number of alarm in one interval - integer
    frequency_interval = 3 #interval in between consecutive alarm at a time in seconds - integer

    catsp = CatSleep()
    catsp.catsleep_control(time_interval, frequency, frequency_interval)


if __name__ == '__main__':
    start_catsleep()
