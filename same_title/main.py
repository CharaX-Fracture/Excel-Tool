from same_title.layout import Layout
from same_title.operate_file import operate_file
from same_title.get_title import get_title
import PySimpleGUI as sg


def same_title():
    layout = Layout.layout

    window = sg.Window('汇总格式相同的文件', layout)

    titles = None
    while True:
        event, values = window.read(timeout=50)

        if event == sg.WIN_CLOSED:
            break
        elif event == 'chosen':
            operate_file(window, values, titles)
        window['path'].update(values['folder'])
        if not titles:
            titles = get_title(window, values) if values['include'] and \
                values['folder'] else None

    window.close()
