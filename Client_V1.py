#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 13:42:05 2023

@author: atsankova
"""
import tkinter as tk
import socket as soc


import socket as soc
client = soc.socket(soc.AF_INET, soc.SOCK_STREAM)  # Création du socket serveur
client.connect(('127.0.0.1', 50000)) # Demande de connexion au serveur
msg = client.recv(1000) # réception de la confirmation de connexion
print(msg.decode())
# Communication
client.send('client connete'.encode())
acc_rcpt = client.recv(1000)
print(acc_rcpt.decode())
# Fermeture

message = ''
while message != 'fin':
    message = input('met :')
    client.send(message.encode())
    acc_rcpt  = client.recv(1000)
    print(acc_rcpt.decode())
    # Fermeture
client.close()










#def valider(evt):
#    bonjour = tk.Label(text="Bonjour !")
#    bonjour.grid(column=2, row=3)
#
#ma_fenetre = tk.Tk()
#ma_fenetre.title("Entrez votre message : ") 
#saisie = tk.Entry(ma_fenetre)
#saisie.pack()
#bouton_entrer = tk.Button(ma_fenetre,text="Envoyer", command= valider(saisie) )
#bouton_entrer.pack()
#ma_fenetre.geometry("800x400") 
#ma_fenetre.mainloop()
#
#client = soc.socket(soc.AF_INET, soc.SOCK_STREAM)  # Création du socket serveur
#client.connect(('172.20.10.208', 50000)) # Demande de connexion au serveur
#msg = client.recv(1000) # réception de la confirmation de connexion
#print(msg.decode())
#client.send('client connete'.encode())
#
## Communication
#
#message = ''
#while message != 'fin':
#    message = input('met :')
#    client.send(message.encode())
#    acc_rcpt  = client.recv(1000)
#    print(acc_rcpt.decode())
#    # Fermeture
#client.close()




