from pytube import YouTube
from openpyxl import Workbook

# create a YouTube object by passing the video URL
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
youtube = YouTube(url)

# print(youtube) 
# get all the available streams for the video
streams = youtube.streams.all()

wb= Workbook()
ws = wb.create_sheet(youtube.title)
ws.append(["title","url"])
# print the video links
for stream in streams:
    ws.append([stream.title,stream.url, stream.itag])
    # print(stream.url)

wb.save("youtube.xlsx")