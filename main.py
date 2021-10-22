import speaker_verification_toolkit.tools as svt
import librosa

print(librosa.load('Known_1.wav'))

data1, sr = librosa.load('Known_2.wav', sr=16000, mono=True)
data2, sr = librosa.load('Known_1.wav', sr=16000, mono=True)

data1 = svt.rms_silence_filter(data1)
data2 = svt.rms_silence_filter(data2)

data1 = svt.extract_mfcc(data1)
data2 = svt.extract_mfcc(data2)

print(
    'The difference between voice1 and voice2 is',
    svt.compute_distance(data1,data2)
)

print(svt.compute_distance(data1, data2))

data3, sr = librosa.load('Unknown.wav', sr=16000, mono=True)
data3 = svt.rms_silence_filter(data3)
data3 = svt.extract_mfcc(data3)

print(svt.compute_distance(data3, data2))

print(svt.find_nearest_voice_data([ data3, data1], data2))
# the index of data1(nearest to data2) is 1 therefore in my case the output is one

# pip install speaker-verification-toolkit
# pip install numba==0.48
# pip install librosa --ignore-installed llvmlite
# Running setup.py install for llvmlite ... error
