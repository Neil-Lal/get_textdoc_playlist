import requests
import csv

# Grab a online editable playlist, parse and create a .txt playlist output

# Variables
path = r'C:\Users\Administrator\Documents\musicbot\Playlists'
filename = r"\surprise playlist.txt"
cert = r'C:\Program Files\Python311\Lib\site-packages\certifi\cacert.pem'
website = "" # Add a download link to website such as textdoc or pastebin

# Download file
req = requests.get(
    url=website, 
    headers={'User-Agent': 'Mozilla/5.0'},
    verify=cert
)

# Decode and grab split text
req.encoding = "utf-8"
file = req.text.split("\n")

# Write to file system
## Assumes text doc is comma seperated and two columns [title, link]
with open(path + filename, "w", encoding="utf-8") as f:
    for row in file:
        line = ['{}'.format(_.strip()) for _ in list(csv.reader([row], delimiter=',', quotechar='"'))[0] ]
        if len(line) == 0 or len(line) == 1 or line[0] == '""' or line[1] == '""' or line[0] == '' or line[1] == '':
            continue
        f.write("# " + line[0] + "\n")
        f.write(line[1] + "\n" + "\n")

