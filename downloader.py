import yt_dlp
import requests

def downloadVideo(url):
    ydlOpts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydlOpts) as ydl:
        ydl.download([url])

def isVideoAvailable(url):
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
        