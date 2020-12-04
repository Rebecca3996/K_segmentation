#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 10:44:27 2020

@author: suraj
"""

import numpy as np
import SimpleITK as sitk
from batchgenerators.utilities.file_and_folder_operations import *


def check_image(img_fname: str):
    npy = sitk.GetArrayFromImage(sitk.ReadImage(img_fname))
    return np.any(np.isnan(npy))


def check_for_nan(input_folder: str):
    nii_files = subfiles(input_folder, suffix='.nii.gz')
    for n in nii_files:
        if check_image(n):
            print("nans found in ", n)