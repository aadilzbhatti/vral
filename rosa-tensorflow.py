#Usage: python <name of this source file> <path to the audio file>


# We'll need numpy for some mathematical operations
import numpy as np


# matplotlib for displaying the output
import matplotlib.pyplot as plt
import matplotlib.style as ms
ms.use('seaborn-muted')

# Librosa for audio
import librosa
# And the display module for visualization
import librosa.display
import sys

    
    
def loadImage(audio_path):
    y, sr = librosa.load(audio_path)

    #make and display a mel-scaled power (energy-squared) spectrogram
    S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)

    # Convert to log scale (dB). We'll use the peak power as reference.
    log_S = librosa.logamplitude(S, ref_power=np.max)

    # Make a new figure
    plt.figure(figsize=(12,4))

    # Display the spectrogram on a mel scale
    # sample rate and hop length parameters are used to render the time axis
    librosa.display.specshow(log_S, sr=sr, x_axis='time', y_axis='mel')

    # Put a descriptive title on the plot
    plt.title('mel power spectrogram')

    # draw a color bar
    plt.colorbar(format='%+02.0f dB')

    # Make the figure layout compact
    #plt.tight_layout()
    # print log_S
    # print sr
    print y
    plt.show()


def convertCoughAudioToText():
    # standard coughing sound
    parent_dir = os.getcwd()
    for root, _, files in os.walk('./coughs/raw'):
        for name in files:
            datapath = os.path.join(root, name)
            y, sr = librosa.load(datapath)
            S = librosa.feature.melspectrogram(y, sr=sr, n_mels = 128)
            np.savetxt(parent_dir + "/coughs/" + name + ".txt", S)


# main()

S = loadImage(sys.argv[1])
    
