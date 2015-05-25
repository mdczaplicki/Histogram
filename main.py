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

def edges():
    out_img = Image.new("L", f.size, None)
    img_data = f.load()
    out_data = out_img.load()
 
    matrix_x = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    matrix_y = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    matrix_size = 3
    matrix_middle = matrix_size/2
 
    rows, cols = f.size
 
    for row in range(rows - matrix_size):
        for col in range(cols - matrix_size):
            pixel_x = 0
            pixel_y = 0
            for i in range(matrix_size):
                for j in range(matrix_size):
                    val = sum(img_data[row+i, col+j])/3
                    pixel_x += matrix_x[i][j] * val
                    pixel_y += matrix_y[i][j] * val
 
            new_pixel = math.sqrt(pixel_x**2 + pixel_y**2)
            new_pixel = int(new_pixel)
            out_data[row + matrix_middle, col + matrix_middle] = new_pixel
 
    out_img.show()
