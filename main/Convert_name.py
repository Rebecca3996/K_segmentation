#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 22:12:00 2020

@author: suraj
"""

    
    
import os 

def main(): 
	
	i=0
	for filename in os.listdir("/mnt/komal/seema/NEW/nnUNet_raw_data_base/nnUNet_raw_data/Task000_Kidney/imagesTr/"): 
		dst =filename[0:15] +".nii.gz" 
		src ='/mnt/komal/seema/NEW/nnUNet_raw_data_base/nnUNet_raw_data/Task000_Kidney/imagesTr/'+ filename 
		dst ='/mnt/komal/seema/NEW/nnUNet_raw_data_base/nnUNet_raw_data/Task000_Kidney/imagesTr/'+ dst 
		
		# rename() function will 
		# rename all the files 
		os.rename(src, dst) 
		i+=1		

# Driver Code 
if __name__ == '__main__':
	# Calling main() function 
	main() 
    