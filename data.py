from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math
import os

import tensorflow as tf


N_MELS = 128


# GET TRAINING DATA
parent_dir = os.getcwd()
training_data_names = [parent_dir + "/coughs/cough2.mp3.txt",
                       parent_dir + "/coughs/cough3.mp3.txt",
                       parent_dir + "/coughs/cough4.mp3.txt",
                       parent_dir + "/coughs/cough5.mp3.txt"]

training_audio_array = []
for f in training_data_names:
    tmp_f = open(f, 'r')
    tmp_mat = [ map(float, line.split(' ')) for line in tmp_f ]
    tmp_mat_transpose = map(list, zip(*tmp_mat))
    training_audio_array.append((tmp_mat_transpose, True))
    tmp_f.close()
    
# # GET DATA FROM FILE
# # first file
# f0 = open(parent_dir + "/test_data/video-0.mp3.txt", 'r')
# l0 = [ map(float, line.split(' ')) for line in f0 ]
# l0_transpose = map(list, zip(*l0))
# #print (l0)


# # real coughing sound
# f_cough = open(parent_dir + "/coughs/cough1.wav.txt", 'r')
# cough = [ map(float, line.split(' ')) for line in f_cough ]
# cough_transpose = map(list, zip(*cough))

# f0.close()
# f_cough.close()

#CREATE VARIABLES IN TENSORFLOW
# tf_l0 = tf.Variable(l0_transpose, name = "tf_l0")
# bias_l0 = tf.Variable(tf.zeros([len(l0_transpose), N_MELS]), name = "bias_l0")

# tf_cough = tf.Variable(l_cough_transpose, name = "tf_cough")
# bias_cough = tf.Variable(tf.zeros([len(l_cough_transpose), N_MELS]), name = "bias_cough")


#(MAYBE, BUT IT'S HORRIBLE) TODO: 1/compare the first row of l_cough_transpose to every row of l0_transpose
# 2/ find the sum of squared differences btw each pair (l_cough_transpose[0][j], l0_transpose[i][j])
# 3/ if the sum of squared differences is within a certain margin of error, start checking if the next size_cough rows below it fits l_cough_transpose. Not more than 5% of rows should have a sum of squared differences outside of allowed margin of error


