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
    im = Image.open(custom_path + str(file))
    im.save(path + "//output//" + str(file) + ".png", format="png", lossless=True)
    nprocessed += 1
    print(f"{str(nprocessed)}/{str(nfiles)}")
