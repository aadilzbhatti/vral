from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math
import os

#import tensorflow as tf


N_MELS = 128 #num_cols

def findMatch(testFile):
    # GET DATA
    parent_dir = os.getcwd()
    data_names = [parent_dir + "/coughs/cough2.mp3.txt",
                  parent_dir + "/coughs/cough3.mp3.txt",
                  parent_dir + "/coughs/cough4.mp3.txt",
                  parent_dir + "/coughs/cough5.mp3.txt"]

    audio_array = []
    for f in data_names:
        tmp_f = open(f, 'r')
        tmp_mat = [ map(float, line.split(' ')) for line in tmp_f ]
        tmp_mat_transpose = map(list, zip(*tmp_mat))
        audio_array.append(tmp_mat_transpose)
        tmp_f.close()


        #TODO: 1/compare the first row of l_cough_transpose to every row of l0_transpose
        # 2/ find the sum of squared differences btw each pair (l_cough_transpose[0][j], l0_transpose[i][j])
        # 3/ if the sum of squared differences is within a certain margin of error, start checking if the next size_cough rows below it fits l_cough_transpose. Not more than 5% of rows should have a sum of squared differences outside of allowed margin of error

        
    
    



