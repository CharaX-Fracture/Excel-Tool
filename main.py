import PySimpleGUI as sg
from keys import Keys

from same_title.main import same_title
from about.main import about


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

        if event == Keys.same_title:
            window.hide()
            same_title()

        elif event == Keys.about:
            window.hide()
            about()

        elif event == sg.WIN_CLOSED:
            break

        window.un_hide()

    window.close()


if __name__ == '__main__':
    main()
