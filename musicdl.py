from pytube import YouTube
import os
from moviepy.editor import *

def ImportVid(url):
    #use youtube module from pytube to enable url input
    import_vid = YouTube(url)
    try:
        import_vid = import_vid.streams.first().download()
        # rename file
        new_vid = r"PATH" #insert absolute path
        os.rename(import_vid, new_vid)
    except:
        print("An error has occurred")
    print("Download complete")

def ChangeVid():
    # previous created file now look in this dir for new file
    for file in os.listdir("./"):
        if file.endswith(".3gpp"):
            gpp_file = file
            mp3_file = "new_song.mp3"  #may rename
            try:
                videoclip = VideoFileClip(gpp_file)
                audioclip = videoclip.audio
                audioclip.write_audiofile(mp3_file)
                audioclip.close()
                videoclip.close()
            except:
                print("An error")
            print("Converted")

url = input("Enter YouTube url: ")
ImportVid(url)
ChangeVid()
