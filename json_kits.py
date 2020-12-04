#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 14:28:40 2020

@author: suraj
"""




from collections import OrderedDict
import os
import json
join = os.path.join

# set data path; Assume that you have prepared the data in `nnUNet_raw_splitted`
label_dir = '/mnt/komal/seema/KIDNEY/My_Data/labelsTr'
output_folder = '/mnt/komal/seema/KIDNEY/My_Data

train_ids=[]
test_ids = []
filenames = os.listdir(label_dir)
filenames.sort()
for name in filenames:
    train_ids.append(name.split('.nii.gz')[0])

add_test_id = True
if add_test_id:
    testnames = os.listdir(join(output_folder,'imagesTs'))
    testnames.sort()
    for test_name in testnames:
        test_ids.append(test_name.split('_000.nii.gz')[0])

# manually set
json_dict = OrderedDict()
json_dict['name'] = "Task00_Kidney" 
json_dict['description'] = "kidney and tumor segmentation"
json_dict['tensorImageSize'] = "4D"
json_dict['reference'] = "KiTs data for nnunet"
json_dict['licence'] = ""
json_dict['release'] = "0.0"
json_dict['modality'] = {
    "0": "CT"
#    "1": "T1", if you have more than on modality
#    "2": "T2"
}
# manually set
json_dict['labels'] = {
    "0": "background",
    "1": "kidney",
    "2": "tumor"
}

json_dict['numTraining'] = len(train_ids)
json_dict['numTest'] = len(test_ids)
json_dict['training'] = [{'image': "./imagesTr/%s.nii.gz" % i, "label": "./labelsTr/%s.nii.gz" % i} for i in train_ids]
json_dict['test'] = ["./imagesTs/%s" % i for i in test_ids]

with open(os.path.join(output_folder, "dataset.json"), 'w') as f:
    json.dump(json_dict, f, indent=4, sort_keys=True)