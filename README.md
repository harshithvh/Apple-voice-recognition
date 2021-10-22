# Apple-voice-recognition
Machine Learning

---

<img align="left" alt="Visual Studio Code" width="820px" height="620px" src="https://zesium.com/wp-content/uploads/2020/12/people-using-voice-recognition_18591-47310.jpg" /> 


### How does Siri work?

---

Siri is based on large-scale Machine Learning systems that employ many aspects of data science.
<br />

Upon receiving your request, Siri records the frequencies and sound
waves from your voice and translates them into a code. Siri then
breaks down the code to identify particular patterns, phrases, and
keywords. This data gets input into an algorithm that sifts through
thousands of combinations of sentences to determine what the
inputted phrase means. This algorithm is complex enough that it is
capable of working around idioms, homophones and other literary
expressions to determine the context of a sentence.

Once Siri determines its request, it begins to assess what tasks
needs to be carried out, determining whether or not the information
needed can be accessed from within the phone’s data banks or from
online servers. Siri is then able to craft complete and cohesive
sentences relevant to the type of question or command requested.

### Technology behind Voice Identification
---
Voice identification technology captures and measures the physical
qualities of a person’s voice when speaking as well as the unique
biological parameters that combine to produce that voice.

<img align="left" alt="Visual Studio Code" width="1080px" src="https://www.iphonelife.com/sites/iphonelife.com/files/heysiri.jpg" />

These parameters Include:

### #1 Pitch 

---

Pitch is an important perceptual dimension by which listeners
discriminate and categorize voice quality. It affects the perceived
brightness of the sound, and brightness may be one of several
perceptual features of a sound used by listeners to distinguish one
voice quality from another.

### #2 Intensity 

---

The increased vocal intensity results from a greater
resistance by the vocal folds to increased airflow. The vocal folds are
blown wider apart, releasing a larger puff of air that sets up a sound
pressure wave of greater amplitude.

### #3 Dynamics

---

Within-person variability in our vocal signals is
substantial: we volitionally modulate our voices to express our
thoughts and intentions or adjust our vocal outputs to suit a
particular audience, speaking environment, or situation.

### Prerequisites

---

On the Terminal run - pip install speaker-verification-toolkit
<br />
On the Terminal run - pip install numba==0.48
<br />
In case an **ERROR** occurs while installing numba==0.48 then :
<br />
On the Terminal run - pip install librosa --ignore-installed llvmlite

### Extra

---

**>** **Numba** is an upgraded version of **Numpy**.
<br />
**>** **Librosa** is a python package for music and audio analysis.
<br />
**>** **svt.rms_silence_filter()** used for filtering environment noise.
<br />
**>** **Mel-Frequency Cepstral Coefficients (MFCC)** feature extraction
method is a leading approach for speech feature extraction that include
**pitch, intensity and dynamics**.
<br />
**>** Known_1, Known_2, Unknown are sample audio voices.
<br />
**>** Covert audio from **.mp4** to **.wav** beacuse librosa supports .wav
<br />
**>** .wav are decompressed files which consume more memory( better quality).
