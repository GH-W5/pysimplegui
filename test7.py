#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/19 5:53
# @Author  : W-gh
# @Site    : 图片浏览器
# @File    : test7.py
# @Software: PyCharm

import PySimpleGUI as sg
import os.path

# 窗口布局两列

file_list_colum = [
    [
        sg.Text("图片文件夹"),
        sg.In(size=(25,1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40,20),
            key="-FILE LIST-"
        )
    ],
]

# 展示选择的文件名字
image_viewer_colum = [
    [sg.Text('Choose an image from the list on the lelf:')],
    [sg.Text(size=(40,1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
]

# ----- 填充布局 -----
layout = [
    [
        sg.Column(file_list_colum),
        sg.VSeparator(),
        sg.Column(image_viewer_colum),
    ]
]

window = sg.Window("图片查看器", layout)

# 事件循环
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # 展示文件名
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # 从文件夹中获取文件名列表
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".tif", ".gif", ".jpg"))
        ]
        window["-FILE LIST-"].update(fnames)
    elif event == "-FILE LIST-":    # 一个文件从列表中被选中
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename=filename)
        except:
            pass


window.close()