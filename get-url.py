from pytube import Playlist
import csv
import pandas as pd

p = Playlist('https://www.youtube.com/playlist?list=PLS1QulWo1RIaJECMeUT4LFwJ-ghgoSH6n')

#print(p.video_urls)

# for url in p.video_urls:
#      print(url)

url=p.video_urls

df = pd.DataFrame(url)
df.to_csv("YoutubeVideoLinks.csv", index=False)

# with open('url-list.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(url)