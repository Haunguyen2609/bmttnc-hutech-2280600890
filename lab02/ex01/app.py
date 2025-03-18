from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayfairCipher  

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods = ["POST"])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()

    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key} <br/>encrypted text:{encrypted_text}"

@app.route("/decrypt", methods = ["POST"])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key} <br/>decrypted text:{decrypted_text}"
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')
@app.route("/vigenere_encrypt", methods = ["POST"])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    vigenere = VigenereCipher()
    encrypted_text = vigenere.encrypted_text(text, key)
    return f"text: {text}<br/>key: {key} <br/>encrypted text:{encrypted_text}"

@app.route("/vigenere_decrypt", methods = ["POST"])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    vigenere = VigenereCipher()
    decrypted_text = vigenere.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key} <br/>decrypted text:{decrypted_text}"
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/rail_fence_encrypt", methods=["POST"])
def rail_fence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])  
    railfence = RailFenceCipher()  
    encrypted_text = railfence.rail_fence_encrypt(text, key)
    return f"text: {text}<br/>key: {key} <br/>encrypted text: {encrypted_text}"

@app.route("/rail_fence_decrypt", methods=["POST"])
def rail_fence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher']) 
    railfence = RailFenceCipher()  
    decrypted_text = railfence.rail_fence_decrypt(text, key)
    return f"text: {text}<br/>key: {key} <br/>decrypted text: {decrypted_text}"
@app.route("/Playfair")
def playfair():
    return render_template('playfair.html')
@app.route("/playfair_encrypt", methods = ["POST"])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    playfair = PlayfairCipher()

    encrypted_text = playfair.playfair_encrypt(text, key)
    return f"text: {text}<br/>key: {key} <br/>encrypted text:{encrypted_text}"

@app.route("/playfair_decrypt", methods = ["POST"])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    playfair = PlayfairCipher()
    decrypted_text = playfair.playfair_decrypt(text, key)
    return f"text: {text}<br/>key: {key} <br/>decrypted text:{decrypted_text}"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)