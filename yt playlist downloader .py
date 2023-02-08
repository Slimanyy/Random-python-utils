from pytube import Playlist

playlist_url = str(input("Enter playlist url: "))
resolution = str(input("Enter Resolution: ") + 'p')

playlist = Playlist(playlist_url)

for videos in playlist.videos:
    videos.streams.get_by_resolution(resolution).download()
    #video.streams.get_highest_resolution().download()
    print(f"{videos.title} is successfully downloaded")

print("\nAll Youtube videos in the playlist have been downloaded succesfully")
