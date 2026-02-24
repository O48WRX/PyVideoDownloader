import yt_dlp
import requests
import os, sys

def getBaseDir(): #Have to add this in case basedir breaks during packaging.
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))

def downloadVideo(url):
    base_dir = getBaseDir()
    ffmpeg_path = os.path.join(base_dir, "bin", "ffmpeg")
    print("Using ffmpeg at:", ffmpeg_path)
    print("Exists:", os.path.exists(ffmpeg_path))
    ydlOpts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'ffmpeg_location': ffmpeg_path,
    }
    try:
        with yt_dlp.YoutubeDL(ydlOpts) as ydl:
            ydl.download([url])
    except Exception as e:
        print("Error:", e)

def isVideoAvailable(url): #Checks video availability based on returned status code
    r = requests.get(url)
    if("Video unavailable" in r.text): return False
    match r.status_code:
        case 200:
            return True
        case _:
            return False
        

def downloadUserInput():
    isURLValid = False
    url = ''
    print('Please provide the URL:')
    while(not isURLValid):
        url = input()
        isURLValid = isVideoAvailable(url)
        if(not isURLValid): print("Please provide a VALID URL:")
    downloadVideo(url)
        