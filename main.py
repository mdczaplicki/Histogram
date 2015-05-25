import sys

__author__ = 'Marek'
from PIL import Image
from PIL import ImageOps
import matplotlib.pyplot as plt
from numpy import sqrt

image = Image.open("image.jpg", mode="r")


def histogram():
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


def grey():
    im_g = image.convert('L')
    im_g.show()
    im_g.save('grey.png', 'PNG')


def roberts():
    out_img = Image.new('L', image.size, None)
    img_data = image.load()
    out_data = out_img.load()
 
    matrix_x = [(-1, 0, 1), (-2, 0, 2), (-1, 0, 1)]
    matrix_y = [(-1, -2, -1), (0, 0, 0), (1, 2, 1)]
    matrix_size = 3
    matrix_middle = matrix_size/2
 
    rows, cols = image.size
 
    for row in range(rows - matrix_size):
        for col in range(cols - matrix_size):
            pixel_x = 0
            pixel_y = 0
            for i in range(matrix_size):
                for j in range(matrix_size):
                    val = sum(img_data[row+i, col+j])/3
                    pixel_x += matrix_x[i][j] * val
                    pixel_y += matrix_y[i][j] * val
 
            new_pixel = sqrt(pixel_x**2 + pixel_y**2)
            new_pixel = int(new_pixel)
            out_data[row + matrix_middle, col + matrix_middle] = new_pixel

    out_img = ImageOps.invert(out_img)
    out_img.show()
    out_img.save('roberts.png', 'PNG')


def main():
    ask = int(input("1. Histogram\n2. Greyscale\n3. Roberts\n"))
    if ask == 1:
        histogram()
    elif ask == 2:
        grey()
    elif ask == 3:
        roberts()

if __name__ == "__main__":
    sys.exit(main())