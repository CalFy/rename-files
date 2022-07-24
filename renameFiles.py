import os
import sys

folder = r'D:\users\nikita\rename\papka'
count = 1
for file_name in os.listdir(folder):
        source = os.path.join(folder, file_name)
        destination = os.path.join(folder, file_name + str(count))
        print(destination)
        os.rename(source, destination)

