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
    #if 'nombre' in voice_data:
        #alexa_speak('Mi nombre es emi')
    if 'note' in voice_data:
        os.system('notepad.exe')
    elif 'paint' in voice_data:
        os.system('mspaint.exe')
    elif 'point' in voice_data:
        os.system('Powerpnt.exe')
    elif 'palabra' in voice_data:
        os.system('winword.exe')
    elif 'control' in voice_data: # en ingles 
        os.system('control.exe')
    elif 'documents' in voice_data:
        os.system('explorer.exe')
    elif 'number' in voice_data:
        os.system('excel.exe')
    elif 'less' in voice_data:
        os.system('calc.exe')
    elif 'movie' in voice_data:#ingles
        os.system('"C:\Program Files\Adobe\Adobe Premiere Pro 2020\Adobe Premiere Pro.exe"')
    elif 'picture' in voice_data:
        os.system('"C:\Program Files\Adobe\Adobe Photoshop CC 2019\Photoshop.exe"')
    elif 'color' in voice_data:#ingles 
        os.system('"C:\Program Files\Adobe\Adobe Illustrator 2020\Support Files\Contents\Windows\Illustrator.exe"')
    elif 'story' in voice_data:
        os.system('"C:\Program Files (x86)\Celtx\celtx.exe"')
    elif 'send' in voice_data:
        os.system('Outlook.exe')
    elif 'bye' in voice_data:
        alexa_speak('Adios')
        exit()

        
alexa_speak('Mi nombre es Emily y te ayudaré a abrir programas de tu computadora. Estos son los programas que puedo abrir')

print('note: block de notas')
print('paint: paint')
print('point: power point')
print('palabra: word')
print('control: panel de control')
print('documents: documentos')
print('number: excel')
print('less: calculadora')
print('movie: premier')
print('picture: photoshop')
print('color: illustrator')
print('story: celtx')
print('send: outlook')
alexa_speak('¿que programa quieres abrir?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
