import os

#os.chdir(r'C:\Users\milic\Desktop\wave\wave\texts\Renamed')
for filename in os.listdir(r'D:\Pycharmprojects\PycharmProjects\youtube_scarping\youtube_audios\audio\wav\otter_download'):
    #delete characters from file
    #os.rename(filename, filename.replace('_otter.ai', ''))
    os.rename(os.path.join(r'D:\Pycharmprojects\PycharmProjects\youtube_scarping\youtube_audios\audio\wav\otter_download', filename), os.path.join(r'D:\Pycharmprojects\PycharmProjects\youtube_scarping\youtube_audios\audio\wav\otter_download', filename.replace('_otter.ai', '')))
    #remove empty files
    #if os.stat(os.path.join(r'C:\Users\milic\Desktop\wave\text1', filename)).st_size == 0:
     #   os.remove(os.path.join(r'C:\Users\milic\Desktop\wave\text1', filename))