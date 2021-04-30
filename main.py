import speech_recognition as sr
import time
import webbrowser
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):
    
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknowValueError:
            print('no entiendo')
        except sr.RequestError:
            print('error de conexion')
        return voice_data

def respond(voice_data):
    if 'como te llamas' in voice_data:
        print('mi nombre es emi')
    if 'hora' in voice_data:
        print(ctime)
    if 'buscar' in voice_data:
        buscar = record_audio('¿que buscas?')
        url = 'https://google.com/search?q=/' + buscar 
        webbrowser.get().open(url)
        print('esto es lo que encontre para: '+ buscar)

    if 'lugar' in voice_data:
        lugar = record_audio('¿que buscas?')
        url = 'https://google.nl/maps/place/' + lugar + '/&amp;'
        webbrowser.get().open(url)
        print('esto es lo que encontre para: '+ lugar)

print('¿en que te ayudo?')
voice_data = record_audio()
while 1:
    voice_data = record_audio
    respond(voice_data)
#print(voice_data)