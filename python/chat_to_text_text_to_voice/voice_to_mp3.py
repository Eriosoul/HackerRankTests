import sounddevice as sd
import soundfile as sf

fs = 44100
duration = 5

print("Habla, estoy grabando...")

recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()

print("Grabación finalizada.")

filename = "grabacion.wav"
sf.write(filename, recording, fs)

print(f"El audio se ha guardado como '{filename}'.")