#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 16:34:58 2023

@author: jwen
"""
from threading import Thread
import socket as soc
import time as tm


annuaire=[]
historique=[]
t = tm.localtime()
def communication(client,client_info):
    global annuaire
    donnees = ''
    while donnees!='fin':
        donnees = client.recv(1000).decode()
        print(client_info, ", message : ", donnees)
        historique.append({"expediteur": client_info, "message": donnees,
                           "jour": f"{t[0]}/{t[1]}/{t[2]}",
                           "time": f"{t[3]}h{t[4]}min{t[5]}s"})
        print(historique)
        client.send('Reçu.'.encode())
    annuaire.remove(client_info)
    print(annuaire)
    client.close() 

serveur = soc.socket(soc.AF_INET, soc.SOCK_STREAM)  # Création du socket serveur
serveur.bind(('0.0.0.0', 50000)) # Association à une adresse IP et un port
serveur.listen()
 # Création d'une file d'attente de connexion
while True:
    (client, client_info) = serveur.accept()
    annuaire.append(client_info)
    print(annuaire)
    client.send('connecté sur le serveur'.encode())
    t1 = Thread(target = communication, args=[client,client_info])
    t1.start()
