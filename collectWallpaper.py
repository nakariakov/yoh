import os
import sys
import urllib


def download_photo(img_url, filename):
    file_path = "%s%s" % ("/Users/marobiana/Documents/pythonTest/", filename)
    downloaded_image = file(file_path, "wb")

    image_on_web = urllib.urlopen(img_url)
    while True:
        buf = image_on_web.read(100000000)
        if len(buf) == 0:
            break
        downloaded_image.write(buf)

    downloaded_image.close()
    image_on_web.close()

    return file_path