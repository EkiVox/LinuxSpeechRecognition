#!/usr/bin/python
# -*- coding: UTF-8 -*-

import yaml
def editcmd():
    i = int(0)
    config = rawconfig["configuration"]
    for listconfig in config:
        print bcolors.OKGREEN + "Ensemble numéro: " + str(i)
        print bcolors.OKGREEN + "   phrase à dire: " + str(listconfig["phrase"])
        print bcolors.OKGREEN + "   réponse de l'ordinateur: " + str(listconfig["answer"])
        print bcolors.OKGREEN + "   commande éxécuté: " + str(listconfig["cmd"])
        i = i+1
    editnum = raw_input(bcolors.OKBLUE + "[+] Chiffre de l'ensemble à édité: ")
    phraseedit = raw_input(bcolors.OKBLUE + "   [+] phrase: ")
    answeredit = raw_input(bcolors.OKBLUE + "   [+] réponse de l'ordinateur: ")
    cmdedit = raw_input(bcolors.OKBLUE + "   [+] commande à executé: ")
    def replace_value_with_definition(key_to_find, valuefinal):
         for key, value in config[int(editnum)].items():
            config[int(editnum)][key_to_find] = valuefinal
    replace_value_with_definition("phrase", phraseedit)
    replace_value_with_definition("cmd", cmdedit)
    replace_value_with_definition("answer", answeredit)
    with open("config.yml", 'w') as recup2:
        yaml.dump(rawconfig, recup2)
    print config
       
        

def removecmd():
    i = int(0)
    config = rawconfig["configuration"]
    for listconfig in config:
        print bcolors.OKGREEN + "Ensemble numéro " + str(i)
        print bcolors.OKGREEN + "   phrase à dire: " + str(listconfig["phrase"])
        print bcolors.OKGREEN + "   réponse de l'ordinateur: " + str(listconfig["answer"])
        print bcolors.OKGREEN + "   commande éxécuté: " + str(listconfig["cmd"])
        i = i+1
    editnum2 = raw_input(bcolors.OKBLUE + "[+] Chiffre de l'ensemble à supprimé: ")
    del rawconfig["configuration"][int(editnum2)]
    with open("config.yml", 'w') as recup2:
        yaml.dump(rawconfig, recup2)


def addcmd():
    config = rawconfig["configuration"]
    phrase_add = raw_input(bcolors.OKGREEN + "   phrase à dire: ")
    answer_add = raw_input(bcolors.OKGREEN + "   réponse de l'ordinateur: ")
    cmd_add = raw_input(bcolors.OKGREEN + "   commande éxécuté: ")
    basic_add = {'answer': 'ceci est un exemple', 'phrase': 'ok ben du coup ca marche!', 'cmd': ''}
    def replace_value_with_definition(key_to_find, valuefinal):
         for key, value in basic_add.items():
            basic_add[key_to_find] = valuefinal
    replace_value_with_definition("phrase", phrase_add)
    replace_value_with_definition("cmd", cmd_add)
    replace_value_with_definition("answer", answer_add)
    config.append(basic_add)
    with open("config.yml", 'w') as recup2:
        yaml.dump(rawconfig, recup2)
    #with open("config.yml", 'w') as recup2:
    #   yaml.dump(rawconfig, recup2)





class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
with open("config.yml", 'r') as recup:
    rawconfig = yaml.load(recup)
print bcolors.OKBLUE + bcolors.BOLD + "[+]" + " écrit le chiffre correspondant à l'action voulu:"
print bcolors.OKBLUE + "    1.Ajouter une commande"
print bcolors.OKBLUE + "    2.Supprimer une commande"
print bcolors.OKBLUE + "    3.Editez une commande"
a = raw_input(bcolors.OKBLUE + "[+] Chiffre de l'action: ")
if a == "1":
    addcmd()
elif a == "2":
    removecmd()
elif a == "3":
    editcmd()
