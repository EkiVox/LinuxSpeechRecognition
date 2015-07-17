#LinuxSpeechRecognition
##Préambule
LinuxSpeechRecognition est une application python utilisant des API tel que PyAudio, SpeechRecognition, etc..
Le but est d'être __modifiable a souhait__

##Installation:
    LinuxSpeechRecognition:
        git clone https://github.com/EkiVox/LinuxSpeechRecognition.git 
        (il sera enregistré dans le dossier LinuxSpeechRecognition/ )
    SpeechRecognition:
        sudo apt-get install python-pip
        sudo pip install SpeechRecognition
    PyAudio:
        sudo apt-get install python-pyaudio
    mpg321:
        sudo apt-get install mpg321
    PyYaml:
        wget http://pyyaml.org/download/pyyaml/PyYAML-3.11.tar.gz
        tar xzvf PyYAML-3.11.tar.gz
        cd PyYAML-3.11
        sudo python setup.py install
    module re, os, urllib:
        installé par défaut avec python
##Utilisation:
    Configuration:
        expliqué dans config.yml
    Lancement:
        cd LinuxSpeechRecognition
        python LinuxSpeechRecognition.py
