from PIL import Image
import pathlib
from os import listdir
from os.path import isfile, join

path = str(pathlib.Path(__file__).parent.absolute())
custom_path = path + "//input//"
onlyfiles = [f for f in listdir(custom_path) if isfile(join(custom_path, f))]
nfiles = len(onlyfiles)
nprocessed = 0
for file in onlyfiles:
    im = Image.open(custom_path + str(file)).convert("RGBA")
    width, height = im.size
    break_loop = False
    for x in range(width):
        for y in range(height):
            alpha = im.getpixel((x, y))[3]
            if alpha != 0:
                startx = x
                starty = y
                break_loop = True
            if break_loop is True:
                break
        if break_loop is True:
            break
    up = starty
    right = startx
    down = starty
    left = startx
    for x in range(width):
        for y in range(height):
            alpha = im.getpixel((x, y))[3]
            if alpha != 0:
                if y < up:
                    up = y
                if y > down:
                    down = y
                if x < left:
                    left = x
                if x > right:
                    right = x

    im = im.crop((left, up, right + 1, down + 1))
    im.save(path + "//output//" + str(file), format="png", lossless=True)
    nprocessed += 1
    print(f"{str(nprocessed)}/{str(nfiles)}")
