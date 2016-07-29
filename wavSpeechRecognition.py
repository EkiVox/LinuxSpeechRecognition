from os import path
import speech_recognition as sr
import yaml
import urllib
import os
import re
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "audio.wav")
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)
text = r.recognize_wit(audio, key="KRBQCEKL3AJQBAKO6ZXIROQ7X4EAJ76L").lower()
print "tu as dit:" + text
with open("config.yml", 'r') as recup:
    config1 = yaml.load(recup)
for config2 in config1["configuration"]:
    answer = config2["answer"]
    cmd = config2["cmd"]
    phrase = config2["phrase"]
    if re.match(phrase , text):
        os.system("espeak -v french -s 150 -p 40 '" + answer + "'")
