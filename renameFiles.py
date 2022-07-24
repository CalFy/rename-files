import os
from datetime import date

today = date.today()
folder = r'D:\users\nikita\rename\papka'
for file_name in os.listdir(folder):
        source = os.path.join(folder, file_name)
        name, ext = os.path.splitext(file_name)
        destination = os.path.join(folder, name + today.strftime("%d_%m_%Y") + ext)
        os.rename(source, destination)
        print(destination)
