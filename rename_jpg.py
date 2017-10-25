import os


#set00_V014_1884.xml
path = '/home/ld/downloads/caltech-pedestrian-converter-master/data/set/set05'
# print os.listdir(path)
for folder in os.listdir(path):
	# print folder
	foldername = folder.split('\\')
	# print  os.listdir(os.path.join(path, folder))
	for file in os.listdir(os.path.join(path, folder)):

		dstname = foldername[0] + '_' + foldername[1] + '_' + file
		dst = os.path.join(path, dstname)
		src = os.path.join(path, folder, file)
		os.rename(src, dst)