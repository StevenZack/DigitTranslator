import numpy
from PIL import Image


def most_common(lst):
    flatList = [el for sublist in lst for el in sublist]
    return max(flatList, key=flatList.count)


def handle(path):
    origin = numpy.asarray(Image.open(path).convert('L').resize((28, 28)))
    bg = most_common(origin)
    print(bg)
    for i, row in enumerate(origin):
        for j, v in enumerate(row):
            if v == bg:
                origin[i][j] = 0
            else:
                origin[i][j] = 255
    img=Image.fromarray(origin)
    img.save('out.png')

handle('in.png')