#rewrite.py
# Rewrite .mp3 files as .txt files with 128 channels (n_mels)

import os
import librosa
import numpy as np

# # test data
# for root, _, files in os.walk('./test_data/raw'):
#     for name in files:
#         datapath = os.path.join(root, name)
#         y, sr = librosa.load(datapath)
#         S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)
#         np.savetxt(os.path.join('..', name + ".txt"), S)


# standard coughing sound
parent_dir = os.getcwd()
for root, _, files in os.walk('./coughs/raw'):
    for name in files:
        datapath = os.path.join(root, name)
        y, sr = librosa.load(datapath)
        S = librosa.feature.melspectrogram(y, sr=sr, n_mels = 128)
        np.savetxt(parent_dir + "/coughs/" + name + ".txt", S)
