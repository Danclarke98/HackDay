import pyaudio
import wave
import numpy as np

CHUNK = 2**11
RATE = 44100

wf = wave.open('/home/poppad/Music/test.wav')

p = pyaudio.PyAudio()


stream = p.open(format =
                p.get_format_from_width(wf.getsampwidth()),
                channels = 1,
                rate = wf.getframerate(),
                input = True)


for i in range(int(10*44100/1024)): #go for a few seconds
    data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
    peak=np.average(np.abs(data))*2
    bars="#"*int(50*peak/2**16)
    print("Int: ", i, "Peak: ", peak, "Bars: ", bars)

stream.stop_stream()
stream.close()
p.terminate()