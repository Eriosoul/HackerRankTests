import speech_recognition as sr

rec = sr.Recognizer()

with sr.Microphone() as mic:
    print('Puede hablar, le escucho...')
    audio = rec.listen(mic)
    print('Tempo terminado')

try:
    texto = rec.recognize_google(audio, language='es')
    print('Texto:', texto)

except Exception as e:
    print('Esto ha explotado', e)