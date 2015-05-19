__author__ = 'Marek'
from PIL import Image
from PIL import ImageDraw
import matplotlib.pyplot as plt

image = Image.open("image.jpg", mode="r")

pix = list(image.getdata())
r = []
g = []
b = []
x = [0] * 768
for p in pix:
    r.append(p[0])
    g.append(p[1])
    b.append(p[2])

for i in range(len(r)):
    x[r[i]] += 1
    x[g[i] + 256] += 1
    x[b[i] + 512] += 1

plt.bar(range(len(x)), x)
plt.show()

im_g = image.convert('L')
im_g.save("a.png", "PNG")