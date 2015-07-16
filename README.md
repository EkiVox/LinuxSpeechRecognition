# LinuxSpeechRecgnition
LinuxSpeechRecognition est un projet de reconnaissance vocale basé sur un fichier de configuration
pour que tout le monde puiss y ajouter ses commandes, phrase, réponse.
Tout est expliqué dans le fichier de configuration (extension .yml) et vous pouvez modifier le code a votre guise (OpenSource) et c'est le principe


Installation (ou plutôt prérequis):
Pour que l'application LinuxSpeechRecognition marche il faut:
    l'api SpeechRecognition:
        sudo apt-get install python-pip
        sudo pip install SpeechRecognition
    PyYaml:
        wget http://pyyaml.org/download/pyyaml/PyYAML-3.11.tar.gz
        tar xzvf PyYAML-3.11.tar.gz
        cd PyYAML-3.11
        sudo python setup.py install
    module os:
        installé par defaut avec python
    module re:
        installé par defaut avec python
    module urllib:
        installé par defaut avec python
