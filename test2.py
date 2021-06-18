#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/18 22:23
# @Author  : W-gh
# @Site    : 
# @File    : test2.py
# @Software: PyCharm

import PySimpleGUI as sg

layout = [[sg.Text('My one-shot window.')],
          [sg.InputText()],
          [sg.Submit(), sg.Cancel()]]

window = sg.Window('Window Title', layout)

event, values = window.read()

window.close()
text_inout = values[0]
sg.popup('You entered ', text_inout)        # 弹出窗口