import os
import sys

folder = r'D:\users\nikita\rename\papka'
count = 1
for file_name in os.listdir(folder):
        destination = file_name + str(count)
        print (destination)
