 
import numpy as np
import scipy.io.wavfile as wav
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog
# DTMF frequencies for each digit
DTMF_FREQS = {
    '1': (1209, 697), '2': (1336, 697), '3': (1477, 697),
    '4': (1209, 770), '5': (1336, 770), '6': (1477, 770),
    '7': (1209, 852), '8': (1336, 852), '9': (1477, 852),
    '*': (1209, 941), '0': (1336, 941), '#': (1477, 941)
}

# Parameters for tone generation
sample_rate = 44100
tone_duration = 0.5  # duration of each tone in seconds
pause_duration = 0.1  # pause duration between tones in seconds

def generate_dtmf_tone(digit, sample_rate, duration):
    if digit not in DTMF_FREQS:
        raise ValueError(f"Invalid digit '{digit}' for DTMF tone generation.")
    
    freqs = DTMF_FREQS[digit]
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    tone = np.sin(2 * np.pi * freqs[0] * t) + np.sin(2 * np.pi * freqs[1] * t)
    return tone

def generate_tone_sequence(number_sequence, sample_rate, tone_duration, pause_duration):
    tones = []
    pause = np.zeros(int(sample_rate * pause_duration))
    for digit in number_sequence:
        tone = generate_dtmf_tone(digit, sample_rate, tone_duration)
        tones.append(tone)
        tones.append(pause)
    return np.concatenate(tones)

# Number sequence "3721"
number_sequence = "3721"

# Generate the tone sequence
tones = generate_tone_sequence(number_sequence, sample_rate, tone_duration, pause_duration)

# Normalize the tones
tones = np.int16(tones / np.max(np.abs(tones)) * 32767)

# Save to a WAV file
wavfile_path = 'generated_dtmf_3721.wav'
wav.write(wavfile_path, sample_rate, tones)
s=blog.solveup("tone",wavfile_path)
print(f"Generated DTMF tones saved to {wavfile_path} {s}")