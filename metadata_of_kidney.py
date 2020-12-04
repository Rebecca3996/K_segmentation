#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 12:41:04 2020

@author: suraj
"""

import os
import numpy as np

from nibabel.testing import data_path
#example_file = os.path.join(data_path, '/home/suraj/Desktop/Task00_Kidney/imagesTr/Kidney_000.nii.gz')
example_file=os.path.join(data_path,'/home/suraj/Desktop/All_abt_kidney/Data_as_downloaded/case_00061/imaging.nii.gz')
import nibabel as nib
img = nib.load(example_file)

header=img.header
print(header)

# data =img.get_data()

# mat = []

# for i in range(img.shape[0]):
#   plane = []
#   for j in range(img.shape[1]):
#     row = []
#     for k in range(img.shape[2]):
#         row.append(data[i][j][k])
#     plane.append(row)
#   mat.append(plane)

