#LinuxSpeechRecognition
##Préambule
LinuxSpeechRecognition est une application python utilisant des API tel que PyAudio, SpeechRecognition, etc..
Le but est d'être __modifiable a souhait__

##Installation:
    script linux (en root):
        apt-get install portaudio19-dev && git clone https://github.com/EkiVox/LinuxSpeechRecognition.git && wget https://pypi.python.org/packages/d0/dc/ffb9ce5e3f19bd289902915a9f68b7d199216065f8ea17d5b5e8e4ad86ee/PyAudio-0.2.9.tar.gz#md5=6d91aae842c7000d2921815e286801fd && tar xzvf Pyaudio-0.2.9.tar.gz && cd PyAudio-0.2.9 && python setup.py install && cd .. && wget http://pyyaml.org/download/pyyaml/PyYAML-3.11.tar.gz && tar xzvf PyYAML-3.11.tar.gz && cd PyYAML-3.11 && python setup.py install && wget https://pypi.python.org/packages/16/5e/62ccc6a4a154e0822f02b3918fb4c666130bf54b2fa4e0a7fa43057c3bf2/SpeechRecognition-3.4.6.tar.gz && tar xzvf SpeechRecognition-3.4.6.tar.gz && cd SpeechRecognition-3.4.6 && python setup.py install && cd.. 
    Packet supplémentaire:
        espeak ( apt-get install espeak)

##Configuration:
    se fait maintenant grace a configurator.py
##Utilisation:
    Lancement:
        cd LinuxSpeechRecognition
        python LinuxSpeechRecognition.py (reconnaisance vocale)
           
    si le dernier ne marche pas, faites:
        cd LinuxSpeechRecognition && arecord audio.wav  (faites Ctrl+C quand vous avez finis)
        python wavSpeechRecognition.py
