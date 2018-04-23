from Crypto.Cipher import AES
import base64

key = bytes("YELLOW SUBMARINE", "ascii")
f = open("7.txt").readlines()
cipher_text = base64.b64decode("".join(f))

obj = AES.new(key, AES.MODE_ECB)
plain_text = obj.decrypt(cipher_text)

print(str(plain_text, "ascii"))
