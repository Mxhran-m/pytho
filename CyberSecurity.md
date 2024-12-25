
# Program 1: SHA-256 Password Hashing
import hashlib
def hash_password(password):
    password_bytes = password.encode('utf-8')
    hash_obj = hashlib.sha256(password_bytes)
    password_hash = hash_obj.hexdigest()
    return password_hash
password = input("Enter password:")
hashed_password = hash_password(password)
print(f"Hashed password: {hash_password(password)}")

# Program 2: Random Password Generator default length 8 chars
import random
import string
def generate_password(length=8):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password
password_length_str = input("Input the desired length of your password:")
if password_length_str:
    password_length = int(password_length_str)
else:
    password_length = 8
password = generate_password(password_length)
print(f"Generated password is: {password}")

# Program 3: Password Validation (!@#$%^&*(),.?:{}|<>)
import re
def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?:{}|<>]', password):
        return False
    return True
password = input("Input your password:")
is_valid = validate_password(password)
if is_valid:
    print("Valid password.")
else:
    print("Not Valid.")


# Program 4: Password File Validator
import re
def check_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True
with open('password.txt', 'r') as f:
    for line in f:
        password = line.strip()
        if check_password(password):
            print(password)


# Program 5: Password Strength the program should consider factors like length, complexity, randomness.
import re
def check_password_strength(password):
    score = 8
    suggestion = []
    if len(password) >= 8:
        score += 1
    else:
        suggestion.append("Password should contain at least 8 characters.")
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestion.append("Password should contain at least one uppercase character.")
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestion.append("Password should contain at least one lowercase character.")
    if re.search(r"\d", password):
        score += 1
    else:
        suggestion.append("Password should contain at least one numeric digit.")
    if re.search(r"[!@#$%^&*(,{}.?/<>|)]", password):
        score += 1
    else:
        suggestion.append("Password should contain at least one special character (!@#$%^&*(),<>.?|{}/).")
    return score, suggestion
password = input("Input a password:")
print(check_password_strength(password))


# Program 6: Password Breach Checker -API
import requests
import hashlib
with open('passwords.txt', 'r') as f:
    for line in f:
        username, password = line.strip().split(',')
        password_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        response = requests.get(f"https://api.pwnedpasswords.com/range/{password_hash[:5]}")
        if response.status_code == 200:
            hashes = [line.split(':') for line in response.text.splitlines()]
            for h, count in hashes:
                if password_hash[5:] == h:
                    print(f"Password for user {username} has been leaked {count} times.")
                    break
            else:
                print(f"Could not check password for user {username}.")


# Program 7: Brute-Force Password Attack Simulator
import itertools
import string
def bf_attack(password):
    char = string.printable.strip()
    attempts = 0
    for length in range(1, len(password) + 1):
        for guess in itertools.product(char, repeat=length):
            attempts += 1
            guess = "".join(guess)
            if guess == password:
                return (attempts, guess)
    return (attempts, None)
password = input("Enter password:")
attempts, guess = bf_attack(password)
if guess:
    print(f"Password cracked in {attempts} attempts. The password is {guess}")
else:
    print(f"Password not cracked after {attempts} attempts.")


# Program 8: symetric encryption using Caesar Cipher Encryption
def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr(ord(char) + shift)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text
plaintext = input("Enter the text to encrypt:")
shift = 3
encrypted_text = caesar_cipher(plaintext, shift)
print("Encrypted Text is:", encrypted_text)


# Program 9: Caesar Cipher Decryption/algorithm.
message = 'YOU ARE BEAUTIFUL'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for key in range(len(LETTERS)):
    translated = ''
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key
            if num < 0:
                num = num + len(LETTERS)
            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol
    print('Key #%s: %s' % (key, translated))


# Program 10: RSA asymmetric Encryption and Decryption
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
keyPair = RSA.generate(3072)
pubKey = keyPair.publickey()
pubkeyPEM = pubKey.exportKey()
privkeyPEM = keyPair.exportKey()
msg = b'Welcome to AIMCA'
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg)
print("Encrypted:", binascii.hexlify(encrypted))
decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)
print("Decrypted:", decrypted.decode('utf-8'))


# Program 11: Base64 Encoding and Decoding
import base64
def base64_encode(text):
    encoded_bytes = base64.b64encode(text.encode('utf-8'))
    encoded_text = encoded_bytes.decode('utf-8')
    return encoded_text
def base64_decode(encoded_text):
    decoded_bytes = base64.b64decode(encoded_text.encode('utf-8'))
    decoded_text = decoded_bytes.decode('utf-8')
    return decoded_text
text_to_encode = "Hello,Base64 Encoding and Decoding!"
encoded_text = base64_encode(text_to_encode)
print("Encoded Text: " + encoded_text)
decoded_text = base64_decode(encoded_text)
print("Decoded Text: " + decoded_text)

# Program 12: Symmetric Encryption using Python Library
from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"Welcome to AIMCA Lab")
print(token)
d = f.decrypt(token)
print(d)
