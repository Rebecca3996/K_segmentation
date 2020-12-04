#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:26:12 2020
@author: suraj
"""

# import nibabel as ni
# img = ni.load('/home/suraj/Desktop/All_abt_kidney/kits19/data/case_00061/imaging.nii.gz')
import os
from nibabel.testing import data_path
example_file = os.path.join(data_path, '/home/suraj/Desktop/imagesTr/prostate_01_0000.nii.gz')

import nibabel as nib
img = nib.load(example_file)
data =img.get_data()

mat = []

for i in range(img.shape[0]):
  plane = []
  for j in range(img.shape[1]):
    row = []
    for k in range(img.shape[2]):
        row.append(data[i][j][k])
    plane.append(row)
  mat.append(plane)
