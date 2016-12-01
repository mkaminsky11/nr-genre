import numpy as np
import pickle
import sys
import os

import librosa
import utils

SOUND_SAMPLE_LENGTH = 30000

HAMMING_SIZE = 100
HAMMING_STRIDE = 40

def getMels(audioPath, id, category):
	print("Generating mels for " + audioPath)

	featuresArray = []
	for i in range(0, SOUND_SAMPLE_LENGTH, HAMMING_STRIDE):
		if i + HAMMING_SIZE <= SOUND_SAMPLE_LENGTH - 1:
			y, sr = librosa.load(audioPath, offset=i / 1000.0, duration=HAMMING_SIZE / 1000.0)

			# Let's make and display a mel-scaled power (energy-squared) spectrogram
			S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)

			# Convert to log scale (dB). We'll use the peak power as reference.
			log_S = librosa.logamplitude(S, ref_power=np.max)

			mfcc = librosa.feature.mfcc(S=log_S, sr=sr, n_mfcc=13)
			# featuresArray.append(mfcc)

			featuresArray.append(S)

			if len(featuresArray) == 599:
				break

	localPath = "mels/{0}/{1}.pp".format(category,id)
	ppFilePath = utils.resolvePath(utils.getPath(),localPath)

	f = open(ppFilePath, 'wb')
	f.write(pickle.dumps(featuresArray))
	f.close()