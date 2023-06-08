from pytube import YouTube #for split audio&video
from youtube_transcript_api import YouTubeTranscriptApi #caption from yt video
from googletrans import Translator #text translator
from gtts import gTTS #text2voice
from moviepy.editor import * # to edit video clips
import os #2play voice
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# url = input("Enter url:")
url = "https://www.youtube.com/watch?v=4FDud9Lj5HY"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
yt = YouTube(url)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
audio = yt.streams.filter(only_audio=True).first() #extract only audio
out_file_a = audio.download(output_path=".") # download the audio
base_a, ext_a = os.path.splitext(out_file_a) # save the audio
new_file_a = base_a + '.mp3'
os.rename(out_file_a, new_file_a)
print("audio extracted")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
video = yt.streams.filter(only_video=True).first() #extract only video
out_file_v = video.download(output_path=".") # download the video
base_v, ext_v = os.path.splitext(out_file_v) # save the video
new_file_v= base_v + '.mp4'
os.rename(out_file_v, new_file_v)
print("video extracted")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def speak(tt): #text to voice convertion 
    translator = Translator()
    mytext = (translator.translate(tt,dest="ta")).text
    myobj = gTTS(text=mytext, lang='ta', slow=False)
    myobj.save("voice.mp3") # os.system("voice.mp3")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
id = (url.split("="))[1]
srt = YouTubeTranscriptApi.get_transcript(id,languages=['en']) #video caption
clip = VideoFileClip(new_file_v)
for i in srt:
    text = i["text"]
    speak(text)
    start = i["start"]                                                           
    audioclip = AudioFileClip("voice.mp3")       #<------converted audiofile name
    videoclip = clip.set_audio(CompositeAudioClip([audioclip.set_start(start)]))
    videoclip.write_videofile("video.mp4")
    clip = VideoFileClip("video.mp4")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("🙂")