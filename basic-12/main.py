from pytubefix import YouTube
from pathlib import Path


# /////////////////////////////
# // Youtube Link from input /
# ////////////////////////////

# This code is a program that helps you download YouTube videos.
#
# 1. It finds your "Downloads" folder on your computer.
# 2. It takes a YouTube link you provide and downloads the video to that folder.
# 3. When you run the program, it asks for the link, downloads the video, and tells you the file name.
#
# In short, it simplifies downloading YouTube videos to your computer.


class MyClass:
    def __init__(self):
        pass

    def download_path(self):
        downloads_path = str(Path.home() / "Downloads")
        save_path = downloads_path
        return save_path

    def download(self, url):
        video = YouTube(url)  # The data here is the url used as an parameter
        video_name = video.title + video.author + ".mp4"
        video.streams.get_highest_resolution().download(
            output_path=self.download_path()
        )
        return video_name


a = MyClass()  # Initializing an instance of the class

print("Download path: ", a.download_path())

# Get URL input from the user
url = input(
    "Please enter a URL: "
)  # What we do with the data
print("Downloading video...")
video_name = a.download(url) # Then we pass the data  url here and use it as argument in our program
print(f"Downloaded: {video_name}")
