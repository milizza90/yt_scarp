# need to have ffmpeg
#pip install wget
#pip install pytube
#pip install pydub
#pip instal numpy
import os
import re
import wget
import numpy as np
from pydub import AudioSegment
from pytube import YouTube

try:
	os.makedirs('./youtube_audios/audio')
	os.makedirs('./youtube_audios/raw_text')
	os.makedirs('./youtube_audios/thumbnail')
except FileExistsError:
	pass

def process_video(path_to_video='https://www.youtube.com/watch?v=BcFLuiqDm8g',
				  main_path='./youtube_audios',
				  captions_lang='en',
				  sample_rate=16000,
				  channels=1,
				  sample_width=2):
	"""
	path_to_video - path to youtube video
	main_path - main directory
	captions_lang - language of captions
	sample_rate - sample_rate in Hz
	channels - 1 (mono) or 2 (stereo)
	sample_width - 1 (8 bits), 2 (16 bits) and etc.
	"""
	yt = YouTube(path_to_video)
	
	# Downloading webm audio
	yt.streams.filter(subtype='webm',only_audio=True).order_by('abr').desc().all()[0].download(output_path=f'{main_path}/audio/')
	
	# Download thumbnail
	thumbnail_url = f'https://img.youtube.com/vi/{yt.video_id}/default.jpg'
	wget.download(thumbnail_url, f'{main_path}/thumbnail/{yt.title}.jpg')
	
	# Convert audio to mp3 and wav we need for training
	audio = AudioSegment.from_file(f"{main_path}/audio/{yt.title}.webm", "webm")
	audio.export(f"./youtube_audios/audio/{yt.title}.mp3", format='mp3', cover=f'{main_path}/thumbnail/{yt.title}.jpg')
	audio.set_frame_rate(sample_rate).set_channels(channels).set_sample_width(sample_width).export(f"{main_path}/audio/{yt.title}.wav", format='wav')
	
	try:
		# Get captions and save it
		caption = yt.captions.get_by_language_code(captions_lang).generate_srt_captions()
		with open(f'{main_path}/raw_text/{yt.title}_original.txt', "w", encoding='utf-8') as text_file:
			text_file.write(caption)
		
		# Get formatted text from captions
		transcript_en = ' '.join(re.sub(r'[0-9]?[\n]?[:,-->]?', '', caption).split('  '))
		with open(f'{main_path}/raw_text/{yt.title}.txt', "w", encoding='utf-8') as text_file:
			text_file.write(transcript_en)
			
	except Exception as error:
		print(error)
		print('Cannot find captions for this video or any other error')
		
if __name__ == "__main__":
	process_video('https://www.youtube.com/watch?v=N4eSCZ1bUNU')
