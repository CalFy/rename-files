import os
from datetime import date

today = date.today()
folder = r'D:\users\nikita\rename\papka'
for file_name in os.listdir(folder):
        source = os.path.join(folder, file_name)
        destination = os.path.join(folder, file_name + today.strftime("%d.%m.%Y"))
        print(destination)
        os.rename(source, destination)
