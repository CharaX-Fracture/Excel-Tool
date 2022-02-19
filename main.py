import PySimpleGUI as sg
from keys import Keys

import same_title.main as st
import about.main as about


def main():
    tool_frame = sg.Frame('可用工具列表', [
        [sg.Button('汇总格式相同的文件', key=Keys.same_title)]
    ])

    layout = [
        [tool_frame],
        [sg.Button('关于我（们）', key=Keys.about)]
    ]

    window = sg.Window('Excel工具', layout)

    while True:
        event, values = window.read()
        window.hide()
        if event == Keys.same_title:
            st.main()

        elif event == Keys.about:
            about.main()

        elif event == sg.WIN_CLOSED:
            break

        window.un_hide()

    window.close()
