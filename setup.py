#!/bin/python3
import urllib.request
import subprocess
dependencies = [
  "markovify",
  "pillow",
  "discord",
  "python-dotenv"
]

print("installing dependencies. running as root reccomended")
for dependency in dependencies:
    print("installing", dependency + "...")
    subprocess.run(["pip", "install", dependency])

print("dependencies installed")

downloads = [
  {
    "url": "https://pasteall.org/i2Y4/raw",
    "filename": "comedy.txt"
  },
  {
    "url": "https://pastebin.com/raw/vmqkry8Z",
    "filename": "shrek.txt"
  },
  {
    "url": "https://pastebin.com/raw/e90ZUNtD",
    "filename": "bee_movie.txt"
  }
]

print("downlading text...")

for download in downloads:
    print("downloading ", download["filename"] + "...")
    request = urllib.request.Request(download["url"])
    response = urllib.request.urlopen(request)
    data = response.read().decode("utf-8")
    file = open(download["filename"], "w")
    file.write(data)
print("text downloaded")

print("setup.py is done.")
print("make sure to put your bot token in .env")
