import os
import random
import sys
from pathlib import Path

if len(sys.argv) < 2:
    print("no directory specified, please input target directory")
    exit()

root_path = sys.argv[1]

xmlfilepath = '.\\datasets\\VOCdevkit\\VOC2012\\Annotations\\'
imagefilepath = '.\\datasets\\VOCdevkit\\VOC2012\\JPEGImages\\'

try:
    os.mkdir(xmlfilepath)
    os.mkdir(imagefilepath)
except:
    pass

total_train = []
total_valid = []
total_test = []
train_subfolder = 'train\\'
valid_subfolder = 'valid\\'
test_subfolder = 'test\\'

for filename in os.listdir(root_path + train_subfolder):
    if filename.endswith('.xml'):
        os.popen(f'copy {root_path + train_subfolder + filename} {xmlfilepath + filename}')
        total_train.append(filename[:-4])
    if filename.endswith('.jpg'):
        os.popen(f'copy {root_path + train_subfolder + filename} {imagefilepath + filename}')

for filename in os.listdir(root_path + valid_subfolder):
    if filename.endswith('.xml'):
        os.popen(f'copy {root_path + valid_subfolder + filename} {xmlfilepath + filename}')
        total_valid.append(filename[:-4])
    if filename.endswith('.jpg'):
        os.popen(f'copy {root_path + valid_subfolder + filename} {imagefilepath + filename}')

for filename in os.listdir(root_path + test_subfolder):
    if filename.endswith('.xml'):
        os.popen(f'copy {root_path + test_subfolder + filename} {xmlfilepath + filename}')
        total_test.append(filename[:-4])
    if filename.endswith('.jpg'):
        os.popen(f'copy {root_path + test_subfolder +filename} {imagefilepath + filename}')


txtsavepath = '.\\datasets\\VOCdevkit\\VOC2012\\ImageSets\\Main'

if not os.path.exists(root_path):
    print("cannot find such directory: " + root_path)
    exit()

if not os.path.exists(txtsavepath):
    os.makedirs(txtsavepath)

print("train size:", len(total_train))
print("valid size:", len(total_valid))
print("test size:", len(total_test))

ftest = open(txtsavepath + '/test.txt', 'w')
ftrain = open(txtsavepath + '/train.txt', 'w')
fval = open(txtsavepath + '/valid.txt', 'w')

ftrain.write('\n'.join(total_train))
fval.write('\n'.join(total_valid))
ftest.write('\n'.join(total_test))

ftrain.close()
fval.close()
ftest.close()
