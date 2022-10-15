# Логгирование,
# дата, время,
# вид операции,
# входные данные,
# выходные данные

from datetime import datetime as dt
from time import time


time = dt.now().strftime("%A %B %d %H:%M:%S %Y")
with open('log.csv', 'a+', encoding="utf-8") as file:
    file.write('Время: ' + time)
