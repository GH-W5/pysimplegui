#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/18 22:31
# @Author  : W-gh
# @Site    : 
# @File    : test3.py
# @Software: PyCharm

import PySimpleGUI as sg

layout = [[sg.Text('Your typed chars appear here:'), sg.Text(size=(15, 1), key='-OUTPUT-')],
          [sg.Input(key='-IN-')],
          [sg.Button('Show'), sg.Button('Exit')]]

window = sg.Window('Pattern 2B', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'Show':
        # 从‘input’的元素更新‘output’元素
        window['-OUTPUT-'].update(values['-IN-'])

window.close()
