#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Topmenu and the submenus are based of the example found at this location http://blog.skeltonnetworks.com/2010/03/python-curses-custom-menu/
# The rest of the work was done by Matthew Bennett and he requests you keep these two mentions when you reuse the code :-)
# Basic code refactoring by Andrew Scheller
import curses, os
from time import sleep
from src import keys_utils, os_utils
from src.log import log
from src.windows import windows_utils

action = 0
open = True

def init():
    try:
        windows_utils.init()
    except Exception as inst:
        v = inst.args[0]
        print('Window size exception. \nSize is %dx%d.\nMinimum size is %dx%d.' % (v['width'], v['height'], v['min_width'], v['min_height']))
        raise

# Main program
def main():
    try:
        init()
        global open
        while True:
            update()
            render()

            if not open:
                break

            sleep(0.05)
            get_input()

        windows_utils.clear()
        exit()
    except Exception as inst:
        print("Unexpected error:", sys.exc_info()[0])
        print(inst)
        print('Exception found.\n Exiting...')
        #raise
        windows_utils.clear()
        exit()

def get_input():
    global action
    active_window = windows_utils.active_window
    action = keys_utils.get_input(active_window)

def update():
    global action
    if action == 'NONE':
        return

    windows_utils.update(action)

    action = 'NONE'

def render():
    windows_utils.render()

def close():
    global open
    open = False
    exit()
