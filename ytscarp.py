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


def process(path_to_video='https://www.youtube.com/watch?v=BcFLuiqDm8g',
				  main_path=os.path.join(os.getcwd(),'youtube_audios'),
				  captions_lang='en',
				  sample_rate=16000,
				  channels=1,
				  sample_width=2):

	yt = YouTube(path_to_video)

	titles = ' '.join(re.sub(r'[0-9]?[\n]?[:,-->]?', '', yt.title).split('  '))

	yt.streams.filter(subtype='webm',only_audio=True).order_by('abr').desc().all()[0].download(output_path=r'D:\Pycharmprojects\PycharmProjects\youtube_scarping\youtube_audios\audio')

	w = os.path.join('path_to_directory', titles) + '.webm'
	audio = AudioSegment.from_file(w, "webm")

	m = os.path.join('path_to_directory', titles) + '.mp3'
	audio.export(m, format = 'mp3')

	v = os.path.join('path_to_directory', titles) + '.wav'
	audio.set_frame_rate(sample_rate).set_channels(channels).set_sample_width(sample_width).export(v, format='wav')

	try:
		# Get captions and save it
		caption = yt.captions.get_by_language_code(captions_lang).generate_srt_captions()

		s = os.path.join('path_to_directory', yt.title) + '_original.txt'
		with open(s, "w", encoding='utf-8') as text_file:
			text_file.write(caption)
		
		# Get formatted text from captions
		transcript_en = ' '.join(re.sub(r'[0-9]?[\n]?[:,-->]?', '', caption).split('  '))

		t = os.path.join('path_to_directory', yt.title) + '.txt'
		with open(t, "w", encoding='utf-8') as text_file:
			text_file.write(transcript_en)
			
	except Exception as error:
		print(error)
		print('Cannot find captions for this video or any other error')

	print(titles)
		

#if __name__ == "__main__":
#	process('https://www.youtube.com/watch?v=WqDiWSL1Zvs')



with open('path_to_directory') as file:
	urls = file.read().splitlines()

for url in urls:
	try:
		process(url)

	except:
		pass

