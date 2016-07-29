from os import path
import speech_recognition as sr
import yaml
import urllib
import os
import re
cmd = ""
answer = ""
r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)
text = r.recognize_wit(audio, key="KRBQCEKL3AJQBAKO6ZXIROQ7X4EAJ76L").lower()
print text
with open("config.yml", 'r') as recup:
    config1 = yaml.load(recup)
for config2 in config1["configuration"]:
    answer = config2["answer"]
    cmd = config2["cmd"]
    phrase = config2["phrase"]
    if re.match(phrase , text):
        params = {
            'tl': 'fr',
            'q': answer,
        }
        encoded = urllib.urlencode(params)
        os.system('mpg321 \"http://translate.google.com/translate_tts?' + encoded + '\"')
        os.system(cmd)
	print(encoded)
