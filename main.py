from skimage import io

img = io.imread('img/red.png')

pixel_num = 0
average = [0, 0, 0]
color = "unclear"

for x_num, x_val in enumerate(img):
    for y_num, y_val in enumerate(x_val):
        average += y_val
        pixel_num += 1

for i, num in enumerate(average):
    average[i] = num / pixel_num

if (average[0]>average[1]+average[2]):
    color = "red"
if (average[1]>average[0]+average[2]):
    color = "green"
if (average[2]>average[0]+average[1]):
    color = "blue"


print("Color: " + color)