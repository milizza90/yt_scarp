import os
import re
import wget
import numpy as np
from pytube import YouTube
from pydub import AudioSegment

dir_path = os.listdir(r'D:\wav')
os.chdir(r'D:\wav')
#dir_path = os.listdir(r'D:\Pycharmprojects\PycharmProjects\youtube_scarping\youtube_audios\audio\wav')
#os.chdir(r'D:\Pycharmprojects\PycharmProjects\youtube_scarping\youtube_audios\audio\wav')

def split_audio(path_without_format,
                split_on_seconds=10,
                audio_format='wav',
                sample_rate=16000,
                channels=1,
                sample_width=2):
    audio = AudioSegment.from_file(f'{path_without_format}.wav', audio_format)
    audio_frames = len(audio)

    c = np.floor(audio_frames / (split_on_seconds * 1000)).astype(np.int)
    """
    if audio_frames < 299999:
        m = audio
        m.set_frame_rate(sample_rate).set_channels(channels).set_sample_width(sample_width).export(
            f'{path_without_format}_part1.wav', format='wav')
    else:
    """
    for i in range(np.floor(audio_frames / (split_on_seconds * 1000)).astype(np.int)-1):
        a = audio[split_on_seconds * 1000 * (i):split_on_seconds * 1000 * (i + 1)]
        a.set_frame_rate(sample_rate).set_channels(channels).set_sample_width(sample_width).export(
            f'{path_without_format}_part{i + 1}.wav', format='wav')

    b = audio[split_on_seconds*1000*(c-1):]
    b.set_frame_rate(sample_rate).set_channels(channels).set_sample_width(sample_width).export(
        f'{path_without_format}_part{c}.wav', format='wav')

    os.remove(path_without_format + '.wav')



if __name__ == "__main__":
    for i in range(len(dir_path)):
        print(dir_path[i][:-4])
       #path = os.path.join(r'D:\Pycharmprojects\PycharmProjects\youtube_scarping\youtube_audios\audio\wav', dir_path[i])
        split_audio(dir_path[i][:-4])
#split_audio(r'C:\Users\Milica (Serenity)\PycharmProjects\youtube_scarping\youtube_audios\audio\wave\Manchester United 2 Tottenham Hotspur 1 Ole Gunnar Post Match Interview')
