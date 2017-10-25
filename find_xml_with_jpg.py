import os
import cv2
path = '/home/ld/downloads/caltech-pedestrian-converter-master/data/annotations/set05'
img_path = '/home/ld/downloads/caltech-pedestrian-converter-master/data/set/set05'
out_path = '/home/ld/downloads/caltech-pedestrian-converter-master/data/image/set05'
# print os.listdir(path)
for file in os.listdir(path):
	# print file.strip('.xml')
	filename = file.strip('.xml') + '.jpg'
	img = cv2.imread(os.path.join(img_path, filename))
	cv2.imwrite(os.path.join(out_path, filename), img)

