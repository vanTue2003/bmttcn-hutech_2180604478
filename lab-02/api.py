from flask import Flask, request, jsonify
from cipher.caersar import CaesarCipher
from cipher.vigenere.vigenere_cipher import VigenereCipher


app = Flask(__name__)

# CAESAR CIPHER ALGORITHM
caesar_cipher = CaesarCipher()
vigenere_Cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods =['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_Cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route('/api/vigenere/decrypt', methods =['POST'])
def vigenere_decrypt():
    data  = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_Cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})
    
@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

# Main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
