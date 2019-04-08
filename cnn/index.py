# -*- coding: utf-8 -*-
"""
@author:HuangJie
@time:18-9-17 下午2:48

"""
import os
import h5py
import numpy as np


import numpy as np
from numpy import linalg as LA

from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input


'''
ap = argparse.ArgumentParser()
ap.add_argument("-database", required=True, help="Path to database which contains images to be indexed")
ap.add_argument("-index", required=True, help="Name of index file")
args = vars(ap.parse_args())
'''

'''
 Returns a list of filenames for all jpg images in a directory. 
'''

'''
def get_imlist(path):
    img_paths = list()
    labels = list()
    class_dirs = sorted(os.listdir(path))
    dict_classid = dict()
    for i in range(len(class_dirs)):
        label = i
        class_dir = class_dirs[i]
        dict_classid[class_dir] = label
        #class_path = os.path.join(path, class_dir)
        class_path = path
        file_names = sorted(os.listdir(class_path))
        for file_name in file_names:
            file_path = os.path.join(class_path, file_name)
            img_paths.append(file_path)
            labels.append(label)
        img_paths = np.asarray(img_paths)
        labels = np.asarray(labels)
    return img_paths, labels

'''
'''
 Extract features and index the images
'''
'''
 Returns a list of filenames for all jpg images in a directory. 
'''


class VGGNet:
    def __init__(self):
        self.input_shape = (224, 224, 3)
        self.weight = 'imagenet'
        self.pooling = 'max'
        self.model = VGG16(weights=self.weight, input_shape=(self.input_shape[0], self.input_shape[1], self.input_shape[2]), pooling=self.pooling, include_top=False)
        self.model.predict(np.zeros((1, 224, 224, 3)))

    '''
    Use vgg16 model to extract features
    Output normalized feature vector
    '''
    def extract_feat(self, img_path):
        img = image.load_img(img_path, target_size=(self.input_shape[0], self.input_shape[1]))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = preprocess_input(img)
        feat = self.model.predict(img)
        norm_feat = feat[0]/LA.norm(feat[0])
        return norm_feat

def get_imlist(path):
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

if __name__ == "__main__":

    #db = args["database"]
    #db = img_paths = './database'
    db = img_paths = 'dataset-retr/train'
    img_list = get_imlist(db)

    print("--------------------------------------------------")
    print("         feature extraction starts")
    print("--------------------------------------------------")

    feats = []
    names = []

    model = VGGNet()
    for i, img_path in enumerate(img_list):
        norm_feat = model.extract_feat(img_path)
        img_name = os.path.split(img_path)[1]
        feats.append(norm_feat)
        names.append(img_name)
        print("extracting feature from image No. %d , %d images in total" %((i+1), len(img_list)))

    feats = np.array(feats)
    names = np.string_(names)
    # directory for storing extracted features
    #output = args["index"]
    output = 'featureCNN.h5'

    print("--------------------------------------------------")
    print("      writing feature extraction results ...")
    print("--------------------------------------------------")

    h5f = h5py.File(output, 'w')
    h5f.create_dataset('dataset_feat', data=feats)
    h5f.create_dataset('dataset_name', data=names)
    h5f.close()
