from pytubefix import YouTube
from pathlib import Path

# /////////////////////////////
# // Youtube Link from input /
# ////////////////////////////
def download_path():
    downloads_path = str(Path.home() / "Downloads")
    save_path = downloads_path 
    return save_path

print("////////  ", download_path())

print("please enter a URL: ")
URL = input()

video = YouTube(URL)
video_name = video.title + ".mp4"
video.streams.get_highest_resolution().download(output_path=download_path())