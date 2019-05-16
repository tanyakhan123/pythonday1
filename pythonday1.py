#This is a tutorial from the book Invent Your
#Own Computer Games with Python

#Caesar cipher
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():#mode function that allows for the computer to understand whether the user wants to encrypt, or decrypt a message
    while True:
        print('Do you wish to encrypt or decrypt a message?')#print statement
        mode = input().lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd']:
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')

def getMessage():
    print('Enter your message: ')#integrates message into cloud
    return input()

def getKey():
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))#sets parameters
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key#reverses the key in order to decrypt
    translated = ''

    for symbol in message:#figures out how to act while encrypting/decrypting message
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1: #Symbol not found in SYMBOLS
            #Just add this symbol without any change
            translated += symbol
        else:
            #Encrypt or decrypt
            symbolIndex += key
        if symbolIndex >= len(SYMBOLS):
            symbolIndex -= len(SYMBOLS)
        elif symbolIndex < 0:
            symbolIndex += len(SYMBOLS)

        translated += SYMBOLS[symbolIndex]
    return translated

mode = getMode()
message = getMessage()
key = getKey()
print('Your translated text is: ')#prints the translated text
print(getTranslatedMessage(mode, message, key))