from gtts import gTTS #pip install gtts

language = "es"
text = "Hola, que tal estas?. Ayer me cai por las escaleras"
speach = gTTS(text=text, lang=language, slow=False, tld="com.au") #converts the text into speech

speach.save("demo1.mp3")