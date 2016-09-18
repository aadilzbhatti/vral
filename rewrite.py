import os
import librosa
import numpy as np

for root, _, files in os.walk('./test_data/raw'):
    for name in files:
        datapath = os.path.join(root, name)
        y, sr = librosa.load(datapath)
        S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)
        np.savetxt(os.path.join('..', name + ".txt"), S)
