from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

pic = Image.open("deer.jpg")

x, y = pic.size
x //= 1
y //= 1

smaller = pic.resize((x, y))
edges = smaller.filter(ImageFilter.FIND_EDGES)
bands = edges.split()

outline = bands[0].point(lambda x: 255 if x<100 else 0)
outline
