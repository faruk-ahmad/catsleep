""" Main module to start the catsleep tool """

import os
import sys

#sys.path.append('./')
from catsleep.catsleep import CatSleep

def start_catsleep():
    """ Starting point of catsleep """

    catsp = CatSleep()
    catsp.catsleep_control()


if __name__ == '__main__':
    start_catsleep()
