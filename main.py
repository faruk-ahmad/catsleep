""" Main module to start the catsleep tool """

import os
import sys

from catsleep.cat import catsleep as ct

def start_catsleep():
    """ Starting point of catsleep """

    catsp = ct.CatSleep()
    catsp.catsleep_control()


if __name__ == '__main__':
    start_catsleep()
