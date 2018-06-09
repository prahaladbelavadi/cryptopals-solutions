# python 2.7

import base64

string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
conv_hex_to_bytes = string.decode("hex")
conv_bytes_to_base64 = conv_hex_to_bytes.encode("base64")
print (conv_bytes_to_base64)
