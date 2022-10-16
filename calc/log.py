# Логгирование,
# дата, время,
# вид операции,
# входные данные,
# выходные данные

from datetime import datetime as dt
from time import time
import __init__ as init

def for_logger():
    time = dt.now().strftime("%A %B %d %H:%M:%S %Y")
    for_log = init.button_click()
    for log in for_log:
        op = log[0]
        data = log[1], log[2]
        result = log[-1]
        with open('log.csv', 'a', encoding="utf-8") as file:
            file.write(f'Время: {time}; Операция: {op}; Входные данные: {data}; Результат: {result} \n')