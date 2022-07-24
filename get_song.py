#Note - Before Start coding you need to install pytube using command - pip install pytube
from pytube import YouTube
import os
import sys
plURL = sys.argv
URL = plURL[1]
yt = YouTube(URL)

try:
    print("\nDownloading....")
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path='../')
    base, ext = os.path.splitext(out_file)
    new_file = base + ".mp3"
    os.rename(out_file, new_file)
    print("\nSuccessfully Downloaded\n")

except:
    print("\nSomething Went Wrong Please Try Again....\n")

