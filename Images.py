__author__ = 'Tena'

from scipy import misc
import numpy as np
import os
from PIL import Image
from os.path import basename

# now you can call it directly with basename



path = os.path.abspath(r'C:\Users\Tena\Documents\Faks\SU\DatasetSviJPG\dataset')

#image = misc.imread("0001.jpg", True)

#print(type(image))
#print(image.shape)
#print(image.dtype)

#C:\Users\Tena\Documents\Faks\SU\OrigDataset\dataset

#import matplotlib.pyplot as plt
#plt.imshow(image, cmap=plt.cm.gray)
#plt.gray()
#plt.imshow(image)
#plt.show()

#for i in range(10):
#    im = np.random.random_integers(1000, ).reshape((100, 100))
#    misc.imsave('random_%02d.png' % i, im)

import glob

#for filename in glob.glob(r'..\..\Documents\Faks\SU\OrigDataset\dataset\*.tiff'):
#     print('%s' % filename)



for filename in os.listdir(path):
    if filename.endswith(".tiff") or filename.endswith(".png"):
        #os.path.join(path, filename)
        #print(os.path.splitext(filename)[0])
        base, ext = os.path.splitext(os.path.join(path, filename))
        Image.open(os.path.join(path, filename)).save(base + '.jpg')
        print(os.path.join(path, filename))
        os.remove(os.path.join(path, filename))
        #print(filename)
        continue
    else:
        continue

'''
min_width = 300
min_height = 300

for filename in os.listdir(path):
    im = Image.open(os.path.join(path, filename))
    width, height = im.size
    if width < min_width and height < min_height:
        min_width = width
        min_height = height

print("Najmanja dimenzija slike je {}x{}".format(min_width, min_height))
'''
#filelist = glob('random*.png')
#filelist.sort()

#print("{} and {}".format(min_width, min_height))