#!/usr/bin/python3

from PySimpleGUI import Window, Text, Button, WIN_CLOSED

layout=[
    [Text("hello")],
    [Button("Ok")]
]

win = Window(title="Hello", layout=layout, margins=(100, 50))

while True:
    event, values = win.read()
    if event == "Ok" or event == WIN_CLOSED:
        break

win.close()
