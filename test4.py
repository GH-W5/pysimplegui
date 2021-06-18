#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/18 22:42
# @Author  : W-gh
# @Site    : 
# @File    : test4.py
# @Software: PyCharm

import PySimpleGUI as sg

# layout = [[sg.Text('A custom progress meter')],
#           [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progressbar')],
#           [sg.Cancel()]]
#
# window = sg.Window('Custom Progress Meter', layout)
# progress_bar = window['progressbar']
# # loop that would normally do something useful
# for i in range(1000):
#     # check to see if the cancel button was clicked and exit loop if clicked
#     event, values = window.read(timeout=10)
#     if event == 'Cancel'  or event is None:
#         break
#     # update bar with loop value +1 so that bar eventually reaches the maximum
#     progress_bar.UpdateBar(i + 1)
# # done with loop... need to destroy the window as it's still open
# window.close()

menu_def = [['File', ['Open', 'Save', 'Exit' ]],
            ['Edit', ['Paste', ['Special', 'Normal',], 'Undo'],]]

# 定义布局
layout = [[sg.Menu(menu_def, tearoff=False, pad=(20,1))],
          [sg.ButtonMenu('ButtonMenu',key='-BMENU-', menu_def=menu_def[0])],]

window = sg.Window('My window with tabs', layout)