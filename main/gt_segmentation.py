#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 11:44:59 2020

@author: suraj
"""

import os
import numpy as np

from nibabel.testing import data_path
#example_file = os.path.join(data_path, '/home/suraj/Desktop/gt_segmentations/hippocampus_001.nii.gz')
#example_file = os.path.join(data_path,'/home/suraj/Desktop/Task04_Hippocampus/Task04_Hippocampus/imagesTr/hippocampus_001_0000.nii.gz')

example_file = os.path.join(data_path,'/home/suraj/Desktop/hippocampus_023_0000_0000.nii.gz')


import nibabel as nib
img = nib.load(example_file)

header=img.header
print(header)