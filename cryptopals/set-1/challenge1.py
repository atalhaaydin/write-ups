from base64 import b64encode
from binascii import unhexlify

a = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

c = unhexlify(a)
# "I'm killing your brain like a poisonous mushroom"
base64_form = b64encode(c)
# SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
print(base64_form)
