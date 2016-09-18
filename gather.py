import os

with open("videos-list", "r") as f:
    os.chdir('test_data')
    for url in f.readlines():
        os.system("youtube-dl --extract-audio --audio-format mp3 --prefer-ffmpeg {}".format(url))
    os.chdir('../')
    return
