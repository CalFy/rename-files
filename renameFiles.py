import os
from datetime import date
import datetime

today = date.today()
folder = r'D:\users\nikita\rename\papka'
for file_name in os.listdir(folder):
        c_date = os.path.getctime(folder)
        dt_c = datetime.datetime.fromtimestamp(c_date).date()
        source = os.path.join(folder, file_name)
        name, ext = os.path.splitext(file_name)
        destination = os.path.join(folder, name + str(dt_c) + ext)
        os.rename(source, destination)
        print(destination)

