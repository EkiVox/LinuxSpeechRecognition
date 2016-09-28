#LinuxSpeechRecognition
##Préambule
LinuxSpeechRecognition est une application python utilisant des API tel que PyAudio, SpeechRecognition, etc..
Le but est d'être __modifiable a souhait__

##Installation:
    script linux (en root):
        apt-get install portaudio19-dev && git clone https://github.com/EkiVox/LinuxSpeechRecognition.git
    Packet supplémentaire:
        espeak ( apt-get install espeak)

##Configuration:
    se fait maintenant grace a configurator
##Utilisation:
    Lancement:
        cd LinuxSpeechRecognition
        ./LinuxSpeechRecognition (reconnaisance vocale)
           
    si le dernier ne marche pas, faites:
        cd LinuxSpeechRecognition && arecord audio.wav  (faites Ctrl+C quand vous avez finis)
        python wavSpeechRecognition.py
