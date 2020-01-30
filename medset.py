import os
import otter_automating
from otter_automating import otter_auto

dir_path = r'D:\wav'
dir_list = os.listdir(dir_path)
os.chdir(r'D:\wav')

try:
    os.makedirs('./otter_download')
except FileExistsError:
    pass

for i in range(80, 100):
    print(dir_list[i])
    file_path = os.path.join(dir_path, dir_list[i])
    otter_auto(file_path)
    print(i)
