## LangSync

## YouTube Video Language Translation
This project allows you to translate the audio of YouTube videos from one language to another. It extracts the audio and video from a given YouTube URL, translates the captions, converts the translated text to speech, and synchronizes it with the video.

## Prerequisites
Before running the code, make sure you have the following packages installed:  
To install the required packages from a requirements.txt file, you can use the following command:

pip install -r requirements.txt

Usage
Open the main.py file.

Uncomment the line url = input("Enter url:") if you want to provide the YouTube URL during runtime. Alternatively, you can directly assign the URL to the url variable.

Run the script.

The code will extract the audio and video from the provided YouTube URL and save them as separate files.

It will then translate the captions of the video using Google Translate and convert the translated text to speech.

The translated audio will be synchronized with the video, and the resulting video with translated audio will be saved.

Once the process is complete, you will see the message "🙂" indicating that the translation process is finished.

## Note
The code currently translates the captions to Tamil (ta) using Google Translate. If you want to translate to a different language, modify the dest parameter in the translator.translate() function call.

Make sure to provide a valid YouTube URL for the url variable.

The code saves the extracted audio as an MP3 file and the final video with translated audio as an MP4 file.
