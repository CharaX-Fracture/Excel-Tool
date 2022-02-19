import openpyxl as xl
import os
from functions import update_output


def get_title(window, values):
    folder_path = values['folder']
    first_file = os.listdir(folder_path)[0]
    file_path = f'{folder_path}/{first_file}'
    sheet = xl.load_workbook(file_path).active
    titles = []
    for row in sheet.iter_rows(max_row=1, values_only=True):
        for cell in row:
            titles.append(cell)

    update_output(window, values, f'已从{first_file}中获取标题')
    window['key'].update(value=titles[0], values=titles)
    return titles
