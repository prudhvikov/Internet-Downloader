from django.shortcuts import redirect, render
from django.http import request
from pytube import YouTube
from django.template.defaultfilters import filesizeformat
from hurry.filesize import size
from django.contrib import messages

def home(request):

    if request.method == "POST":
       try:
        url = request.POST.get('url')
        yt  = YouTube(url)
        video_streams = yt.streams.filter(progressive=True)
        audio_streams = yt.streams.filter(only_audio=True)
        video = []
        audio = []

        for i in range(3):
          if i == 0:
            continue
          video.append(video_streams[i])
        
        for j in range(2):
            audio.append(audio_streams[j])

        context = {
            'yobj' : yt,
            'video_streams' : video,
            'audio_streams' : audio,
        }    
        return render(request,'youtube-downloader.html',context)
       except: 
        messages.error(request, 'The URL seems to be not valid, please try another URL')      
    return render(request,'youtube-downloader.html')
