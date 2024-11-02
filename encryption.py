# encryption using a linear feedback shift register
import bindec


# converts a character c into a list of six 1's and 0's using Base64 encoding
def charToBin(c):
    ascii_code = ord(c)
    if c.isupper():
        base64_code = ascii_code - 65
    elif c.islower():
        base64_code = ascii_code - 71
    elif c == '+':
        base64_code = 62
    elif c == '/':
        base64_code = 63
    else:
        base64_code = ascii_code + 4

    binary = bindec.decToBin(base64_code)
    return binary


# converts a list of six 1's and 0's into a character using Base64 encoding
def binToChar(b):
    binary = bindec.binToDec(b)
    if binary <= 25:
        char = chr(binary + 65)
    elif binary <= 51:
        char = chr(binary + 71)
    elif binary == 62:
        char = '+'
    elif binary == 63:
        char = '/'
    else:
        char = chr(binary - 4)
    return char


# convert a string of characters into a list of 1's and 0's using Base64 encoding
def strToBin(s):
    binary = []
    for char in s:
        binary += charToBin(char)
    return binary


# convert a list of 1's and 0's into a string of characters using Base64 encoding
def binToStr(b_list):
    i = 0
    result = ""
    while i < len(b_list) - 5:
        char_bin = b_list[i:i + 6]
        result += binToChar(char_bin)
        i += 6
    return result


# generates a sequence of pseudo-random numbers
def generatePad(seed, k, length):
    prl = []
    while len(prl) < length:
        xor = seed[0] ^ seed[-k]
        seed.pop(0)
        seed.append(xor)
        prl.append(seed[-1])
    return prl


# takes a message and returns it as an encrypted string using an [N, k] LFSR
def encrypt(message, seed, k):
    bin_list = strToBin(message)
    lfsr = generatePad(seed, k, len(bin_list))
    bin_cipher = []
    for i in range(len(bin_list)):
        bin_cipher.append(bin_list[i] ^ lfsr[i])
    ciphertext = binToStr(bin_cipher)
    return ciphertext

