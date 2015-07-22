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
##Configuration:
    la configuration marche de la maniere suivante:
    Il ne doit pas avoir de majuscule dans phrase!
    2 espaces, tiret, a la ligne, 4 espace puis phrase, a la ligne 4 espace puis answer, a la ligne 4 espace puis cmd     obligatoirement. si vous ne savez pas quoi mettre laisse vide. Exemple:
    
      -
        phrase: lance chrome
        cmd: chromium-browser
        answer: chrome se lance
      -
        phrase: (lance|ouvre) le client (ftp|sftp)       [la, si on dit lance ou ouvre ca revient au même, pareil pour ftp ou sftp. c'est grace au "()" et "|"]
        cmd: filezilla
        answer: Le client ftp se lance
    
        

##Utilisation:
    Lancement:
        cd LinuxSpeechRecognition
        python LinuxSpeechRecognition.py
