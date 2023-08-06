# Written by: Mr.Py AKA GhostByte on GitHub
# Date: 2023-08-06
import yt_dlp
import os

def play_youtube_video(video_link):
  """Plays the audio from the specified YouTube video."""
  ydl_opts = {
    "format": "bestaudio",
    "outtmpl": "audio.mp3",
    "verbose": True,
  }
  with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_link])

  # Try to open the audio file in Windows Media Player Legacy.
  try:
    # If not on a Windows operating system, this will raise a FileNotFoundError.
    os.system("wmplayer audio.mp3")
    # The `os.startfile()` function is not available on non-Windows systems.
    # If Windows Media Player Legacy is installed, open the audio file in it.
  except FileNotFoundError:
    # If Windows Media Player Legacy is not installed, try opening the audio file in VLC.
    os.system("vlc audio.mp3")

if __name__ == "__main__":
  YT = input("Enter the YouTube video link:")
  print("Playing audio from YouTube video...")
  play_youtube_video(YT)
print("Done!")