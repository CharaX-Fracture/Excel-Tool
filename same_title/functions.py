import time


def now_time():
    now = time.localtime()
    time_str = f'[{now.tm_hour}:{now.tm_min}:{now.tm_sec}]'
    return time_str


def update_output(window, values, add_value):
    output = values['output'] + f'\n{now_time()}{add_value}'
    window['output'].update(output)


def update_title(window, titles):
    window['key'].update(''.join(titles))
