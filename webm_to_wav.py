import os
from pydub import AudioSegment

os.chdir(r'D:\medset')

list = os.listdir()

for i in range(len(list)):
    audio = AudioSegment.from_file(list[i],'webm')
    file_mp3 = list[i][:-4]+'mp3'
    audio.export(file_mp3, format = 'mp3')
    file_wav = list[i][:-4]+'wav'
    audio.set_frame_rate(16000).set_channels(1).set_sample_width(2).export(file_wav, format = 'wav')
    print(i)

