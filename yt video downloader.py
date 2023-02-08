from pytube import YouTube

video_url = str(input("Enter youtube video url: "))
resolution = str(input("Enter Resolution: ") + 'p')
video = YouTube(video_url)
#The video will only be downloaded if the resolution specified is available
video_stream = video.streams.get_by_resolution(resolution)
#video_stream = video.streams.get_highest_resolution()
video_stream.download()

print("Youtube video downloaded succesfully")