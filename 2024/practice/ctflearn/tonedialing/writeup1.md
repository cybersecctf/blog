<title>ctf event- challengename Challenge Writeup(first save it)</title>

<!DOCTYPE html>
<html>

<body>
    <h1>ctf event- challengename Challenge Writeup(first save it)</h1>

    <h2>Challenge Description</h2>
    <p> At 1pm I called my uncle who was 64 years old 10 months ago, but I heard only that. Later I started thinking about the 24 hour clock.

I hope you will help me solve this problem
 <a href="https://ctflearn.com/challenge/download/889">you_know_what_to_do.wav</a>
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
we use this python code for conver wav to numbers
<pre>
#python
import blog
import numpy as np
import scipy.io.wavfile as wav
from scipy.signal import find_peaks
from scipy.fft import fft
from itertools import groupby

# DTMF frequencies for each digit
DTMF_FREQS = {
    (1209, 697): '1', (1336, 697): '2', (1477, 697): '3',
    (1209, 770): '4', (1336, 770): '5', (1477, 770): '6',
    (1209, 852): '7', (1336, 852): '8', (1477, 852): '9',
    (1209, 941): '*', (1336, 941): '0', (1477, 941): '#'
}

# Load the wav file

def solve(file_path):
 rate, data = wav.read(file_path)
 # If stereo, take one channel
 if len(data.shape) == 2:
    data = data[:, 0]
 # Normalize the data
 data = data / np.max(np.abs(data))

 # Parameters
 window_size = int(0.1 * rate)  # 100 ms window
 step_size = int(0.05 * rate)   # 50 ms step

 # Function to find the closest DTMF tone
 def find_dtmf_tone(freqs, magnitudes):
    threshold = 0.1 * np.max(magnitudes)  # Lower threshold for detection
    peaks, _ = find_peaks(magnitudes, height=threshold)
    peak_freqs = freqs[peaks]
    detected_tones = []
    for f1, f2 in DTMF_FREQS.keys():
        if any(np.isclose(peak_freqs, f1, atol=10)) and any(np.isclose(peak_freqs, f2, atol=10)):
            detected_tones.append(DTMF_FREQS[(f1, f2)])
    return detected_tones

 # Segment the audio and analyze each segment
 detected_digits = []
 for start in range(0, len(data) - window_size, step_size):
    segment = data[start:start + window_size]
    freqs = np.fft.fftfreq(len(segment), 1/rate)
    magnitudes = np.abs(fft(segment))

    # Only consider positive frequencies
    freqs = freqs[:len(freqs)//2]
    magnitudes = magnitudes[:len(magnitudes)//2]

    digits = find_dtmf_tone(freqs, magnitudes)
    if digits:
        detected_digits.extend(digits)
 return ''.join(detected_digits)
# Combine detected digits into a string
file_path = blog.set('you_know_what_to_do.wav',1)
detected_number =solve(file_path)#get detect numbers from wav
print("Detected number:", detected_number)

# Example usage:
original_number = "667778444777011108111011199977711111101112333666777828999808444777999777111826665807772899911125"
simplified_result =simplified_result = "".join(ch for ch, _ in groupby(original_number))
print(simplified_result)
#make unique and then defragment on base of wav and ascii numbers and create fragments of ascii number 

# Fragment the detected number based on the given pattern
fragments = [67, 84, 70, 108, 101, 97, 110, 123,
             67, 82, 89, 80, 84, 79, 71, 82,
             65, 80, 72, 89, 125]

# Convert each fragment to its ASCII character
ascii_characters = [chr(fragment) for fragment in fragments]

# Join the characters to form the decoded message
decoded_message = ''.join(ascii_characters)

print("Decoded message:", decoded_message)


</pre>
67847010810197110123678289808479718265807289125     that should manually split to 67 84 70 108 101 97 110 123 67 82 89 80 84 79 71 82 65 80 72 89 125       and convert this number to char like this <a href="https://cybersecctf.github.io/blog/2024/practice/picoctf/thenumbers/writeup1.md">writeup</a> for get   flag
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">CTFlean{CRYPTOGRAPHY}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on decode tone dialing with python </p>
</body>
</html>



