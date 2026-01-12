# Python Ransomware Simulation (Educational)

This repository contains a functional simulation of a ransomware attack and its corresponding recovery tool. This project was developed to explore **cryptography**, **file system manipulation**, and **cybersecurity defense mechanisms** using Python.

> **ATTENTION:** This project is for **educational and research purposes only**. Unauthorized use of this code is strictly prohibited and illegal. Always run this in a secure, isolated virtual environment.


##  Project Structure

* `voldemort.py`: The "Malware" script. It discovers files, generates a unique encryption key, and locks the data.
* `decryptor.py`: The "Recovery" script. It requires a specific passphrase to unlock the files.
* `thekey.key`: The symmetric key generated during encryption (created at runtime).

##  How it Works

### 1. Discovery & Encryption (`voldemort.py`)
The script uses the `os` module to list all files in its directory. It specifically ignores the script itself and the key file to prevent "self-locking." It then:
* Generates a symmetric key using the **Fernet (AES)** algorithm.
* Reads the binary content of target files.
* Overwrites the files with encrypted ciphertext.

### 2. Authentication & Decryption (`decryptor.py`)
To reverse the process, the user must provide the hardcoded passphrase:
* **Passphrase:** `enisistourist`
* If correct, the script reads `thekey.key` and decrypts the files back to their original state.

---

## 🛠️ Installation

You need the `cryptography` library to run these scripts:

bash
pip install cryptography
