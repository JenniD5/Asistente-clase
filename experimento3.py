import speech_recognition as sr
import time 
import webbrowser
import playsound
import os
import random 

from gtts import gTTS
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            #print(ask)
            alexa_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)

        except sr.UnknownValueError:
            alexa_speak('Lo siento, no te entendi')
        except sr.RequestError:
            alexa_speak('Lo siento, error de conexion')
        return voice_data

def alexa_speak(audio_string):
    tts = gTTS(text = audio_string, lang='es')
    r = random.randint(1, 10000000)
    audio_file = 'audio-'+ str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'nombre' in voice_data:
        alexa_speak('Mi nombre es alexis')
    if 'hora' in voice_data:
        alexa_speak(ctime())
    if 'buscar' in voice_data:
        buscar = record_audio('Que necesitas buscar?')
        url = 'https://google.com/search?q=' + buscar
        webbrowser.get().open(url)
        alexa_speak('Esto fue lo que encontre para: ' + buscar)
    if 'place' in voice_data:
        lugar = record_audio("Que lugar?")
        url = 'https://google.nl/maps/place/' + lugar + '/&amp;'
        webbrowser.get().open(url)
        print('Es lo que encontre para:' + lugar)
    if 'color' in voice_data:
        color = record_audio('¿Que color?')
        url = 'https://google.com/search?q=' + color
        webbrowser.get().open(url)
        alexa_speak('Esto es lo que encontre para: ' + color )
    if 'noticias' in voice_data:
        noticia = record_audio('¿Que noticias?')
        url = 'https://google.com/news?=' + noticia
        webbrowser.get().open(url)
        alexa_speak('Esto es lo que encontre para: ' + noticia )
    if 'abajo' in voice_data:
        exit()
#time.sleep(1)
alexa_speak('Como te puedo ayudar')
while 1:
    voice_data = record_audio()
    respond(voice_data)
