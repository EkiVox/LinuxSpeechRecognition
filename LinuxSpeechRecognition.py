#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time

from os import path
import speech_recognition as sr
import yaml
import urllib
import os
import re
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
cmd = ""
answer = ""
r = sr.Recognizer()
with sr.Microphone() as source:
    cls()
    r.adjust_for_ambient_noise(source)
    cls()
    print bcolors.OKGREEN + "Parle à partir de maintenant!"
    audio = r.listen(source)
    cls()
    print bcolors.OKGREEN + "C'est bon!"
try:
    text = r.recognize_wit(audio, key="KRBQCEKL3AJQBAKO6ZXIROQ7X4EAJ76L").lower()
    cls()
    print bcolors.OKBLUE + bcolors.BOLD + "je pense que tu as dit: " + text + "! Maintenant je vais verifier la correspondance avec le fichier de configuration"
except sr.UnknownValueError:
    cls()
    print("Impossible de comprendre")
time.sleep(1)
with open("config.yml", 'r') as recup:
    config1 = yaml.load(recup)
for config2 in config1["configuration"]:
    answer = config2["answer"]
    cmd = config2["cmd"]
    phrase = config2["phrase"]
    if re.match(phrase , text):
        os.system("espeak -v french -s 150 -p 40 '" + answer + "'")
        os.system(cmd)
execfile("LinuxSpeechRecognition.py")
