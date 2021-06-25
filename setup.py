#!/bin/python3
import urllib.request
import subprocess
import os

print("installing dependencies. running as root reccomended")


subprocess.run(["pip", "install", "-r", "requirements.txt"])

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

print("checking if token env var exists...")

try:
    token = os.environ["TOKEN"]
    file = open(".env", "w")
    file.write("TOKEN=" + token)
except Exception:
    print("token does not exist or other error")
    print("manually put your token in .env")

print("setup.py is done.")
