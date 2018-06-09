# Fixed XOR

def XORstringBuffer(string1, string2):
    if (len(string1)==len(string2)):
        print(str.encode(string1)^str.encode(string2))
    else:
        return "string length aren't the same"

XORstringBuffer("1c0111001f010100061a024b53535009181c","686974207468652062756c6c277320657965")
