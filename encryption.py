from math import floor
import base64

def xor(key,plaintext):
    result = []
    k =  None
    try:
        key = int(key)
        k = key
    except ValueError:
        current_index_key = 0
        length_key = len(key)
    for byte in plaintext:
        if type(key) == str:
            k = ord(key[current_index_key])
            current_index_key+=1
            current_index_key%=length_key
        result.append(ord(byte) ^ k)
    return result

def caesar_cipher(key,plaintext): 
    result = []
    key %= 26
    for byte in plaintext:
        byte = ord(byte)
        res = byte + key
        if byte >= 97 and byte <= 122:
            if res > 122:
                res = res % 122 + 96
        else:
            if res > 90:
                res = res % 90 + 64
        result.append(res)

    return result 
