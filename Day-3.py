
#File Open & Read 
"""
file = open('vansh.txt', 'r')
content = file.read()
line = file.readline()
line = file.readlines()
print(content)
file.close()
"""
#File Write & Open
"""
file = open('vansh.txt', 'w')
file.write("Thanks me later once the task been completed\n ")
"""
#appending
"""
file = open('vansh.txt', 'a')
"""

import os
#os.mkdir('folder1')
"""
a = os.listdir('.')
print(a)
"""
#check the file&folder exist or not
"""
import os.path
x = os.path.exists('vansh.txt')
print('The File exist in: ', x)

#Remove Folder
os.rmdir('folder1')
a = os.listdir('.')
print(a)
"""

import shutil
shutil.rmtree