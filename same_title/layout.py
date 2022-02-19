import PySimpleGUI as sg


class Layout:
    layout = [
        [sg.FolderBrowse('选择源文件夹', key='folder')],
        [sg.Text('已选择：'), sg.Text('', key='path')],
        [sg.Radio('有标题', 'title?', key='include', default=True),
         sg.Text('请选择关键字（若有标题）：'),
         sg.Combo([], key='key', size=(10, 4))],
        [sg.Radio('没标题', 'title?', key='not_include')],
        [sg.Button('选好了', key='chosen')],
        [sg.Frame('程序输出', [[sg.Multiline('', key='output')]])]
    ]
