import argparse
from encryption import *

parser = argparse.ArgumentParser()

parser.add_argument("-e","--enc",type=str,metavar="xor",help="Encode/Encrypt as")
parser.add_argument("-k","--key",type=str,help="Encryption key")
parser.add_argument("-p","--plaintext",type=str,help="Plaintext that will be encrypted")
parser.add_argument("-l","--list",action='store_true',help="List all available encryption algorithms")

args = parser.parse_args()

def print_result(result):
    hex_r = ""
    dec_r = "" 
    ascii_r = ""
    for _ in result:
        hex_r += hex(_) + " "
        ascii_r += chr(_) 
        dec_r += str(_)  + " "
    print()
    print("[+] Hex Representation : " + hex_r)
    print("[+] Decimal Representation : " + dec_r)
    print("[+] Ascii Char Representation : " + ascii_r)

if args.list ==  True:
    algorithms = ['xor','caesar_cipher','rot13','html','url','base64']
    print("[+] Available Encryption algorithms : ")
    for algorithm in algorithms:
        print("   > " + algorithm)

    exit()

if args.enc == None:
    print("[!] You have to specify the encryption algorithm")
    exit()
if args.key == None and args.enc in ['xor','caesar_cipher']:
    print("[!] You have to specify the encryption key")
    exit()
if args.plaintext == None :
    print("[!] You have to specify the plaintext")
    exit()

result = None


if args.enc == 'xor':
    result = xor(args.key,args.plaintext)
elif args.enc == 'caesar_cipher':
    try:
        key = int(args.key)
    except ValueError: 
        print("[!] The encryption key must be an integer value")
        exit()
    result = caesar_cipher(key,args.plaintext)
elif args.enc == 'rot13':
    if args.key != None:
        print("[!] You don't have to specify the encryption key")
    result = caesar_cipher(13,args.plaintext)
elif args.enc == 'html':
    result = "".join([hex(ord(i)) + ";" for i in args.plaintext]).replace("0x","&#x")
    print("Result : " + result)
    exit()
elif args.enc == 'url':
    result = "".join([hex(ord(i)) for i in args.plaintext]).replace("0x","%")
    print("Result : " + result)
    exit()
elif args.enc == 'base64':
    pass
else:
    print("[!] The encryption algorithm that you have specified is not available")
    exit()

print_result(result)
