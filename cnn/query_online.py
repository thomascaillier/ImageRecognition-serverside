#!bin/bash
#*#* -*- coding: utf-8 -*-
"""
@author:HuangJie
@time:18-9-17 下午2:48

"""


import numpy as np
import h5py
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from app.models import Image, CorrespondingImages
import argparse
import os
import io
from PIL import Image

'''
ap = argparse.ArgumentParser()
ap.add_argument("-query", required=True, help="Path to query which contains image to be queried")
ap.add_argument("-index", required=True, help="Path to index")
ap.add_argument("-result", required=True, help="Path for output retrieved images")
args = vars(ap.parse_args())
'''

def read_images(url):
    with open(url, "rb") as _image:
        f = _image.read()
        b = bytearray(f)
        return b


def analyse_image(image):
    # read in indexed images' feature vectors and corresponding image names
    #h5f = h5py.File(args["index"], 'r')
    os.chdir(os.path.dirname(__file__))
    h5f = h5py.File('featureCNN.h5', 'r')
    feats = h5f['dataset_feat'][:]
    imgNames = h5f['dataset_name'][:]
    h5f.close()

    print("--------------------------------------------------")
    print("               searching starts")
    print("--------------------------------------------------")

    # read and show query image
    #queryDir = args["query"]
    #queryDir = './database/001_accordion_image_0001.jpg'

    image_bytes = read_images(image.base_image)
    img = Image.open(io.BytesIO(image_bytes))  # on
    img.save('test.jpeg')


    # queryImg = mpimg.imread(queryDir)
    # plt.figure()
    # plt.subplot(2, 1, 1)
    # plt.imshow(queryImg)
    # plt.title("Query Image")
    # plt.axis('off')

    # init VGGNet16 model
    from cnn.extract_cnn_vgg16_keras import VGGNet
    model = VGGNet()

    # extract query image's feature, compute simlarity score and sort
    queryVec = model.extract_feat('test.jpeg')
    scores = np.dot(queryVec, feats.T)
    rank_ID = np.argsort(scores)[::-1]
    rank_score = scores[rank_ID]
    #print(rank_score)


    # number of top retrieved images to show
    maxres = 3
    imlist = [imgNames[index] for i, index in enumerate(rank_ID[0:maxres])]

    for i, im in enumerate(imlist):
        image = mpimg.imread('./dataset-retr/train'+"/"+im.decode('utf-8'))
        plt.subplot(2, 3, i+4)
        plt.imshow(image)
        plt.title("search output %d" % (i + 1))
        plt.axis('off')
    plt.show()

    im = imlist[0]
    im0 = im.decode('utf-8')
    score0 = sorted(scores, reverse=True)[0]

    ima = imlist[1]
    im1 = ima.decode('utf-8')
    score1 = sorted(scores, reverse=True)[1]

    imb = imlist[2]
    im2 = imb.decode('utf-8')
    score2 = sorted(scores, reverse=True)[2]

    list0 = [im0, score0]
    list1 = [im1, score1]
    list2 = [im2, score2]

    firstimage = str(list0)
    secondimage = str(list1)
    thirdimage = str(list2)


    return (im0, score0, im1, score1, im2, score2)
