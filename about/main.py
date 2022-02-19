import PySimpleGUI as sg
import webbrowser
from about.keys import Keys


def about():
    me_frame = sg.Frame('关于作者', [
        [sg.Button('B站', key=Keys.bili)],
        [sg.Text('QQ:')]
    ])

    layout = [
        [sg.Text('Excel工具')],
        [me_frame]
    ]

    window = sg.Window('关于', layout)

    while True:
        event, values = window.read()

        if event == Keys.bili:
            webbrowser.open('https://space.bilibili.com/517691213')

        elif event == sg.WIN_CLOSED:
            break

    window.close()
