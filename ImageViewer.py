import PySimpleGUI as sg
import os.path

file_list = [
    [
        sg.Text('Image Folder'),
        sg.In(size=(25, 1), enable_events=True, key='-FOLDER-'),
        sg.FolderBrowse()
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20),
            key='-FILE-LIST-'
        )
    ],
]

image_viewer = [
    [sg.Text('Choose a file from the left: ')],
    [sg.Text(size=(40, 1), key='-TOUT-')],
    [sg.Image(key='-Image-')],
]
lo = [
    [
        sg.Column(file_list),
        sg.VSeparator(),
        sg.Column(image_viewer),
    ]
]

win = sg.Window('Image Viewer', layout=lo)
while True:
    event, values = win.read()
    if event == 'EXIT' or event == sg.WIN_CLOSED:
        break
    if event == '-FOLDER-':
        folder = values['-FOLDER-']
        try:
            files = os.listdir(folder)
        except FileNotFoundError or IOError:
            files = []
            fnames = [
                f
                for f in files
                if os.path.isfile(os.path.join(folder, f))
                and f.lower().endswith(('.png', '.gif'))
            ]
            win['FILE-LIST-'].update(fnames)
    elif event == 'FILE-LIST-':
        try:
            filename = os.path.join(
                values['-FOLDER-'], values['-FILE-LIST-'][0]
            )
            win['FILE-LIST-'].update(filename)
            win['-Image-'].update(filename=filename)
        except:
            pass
win.close()
