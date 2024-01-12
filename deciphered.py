def decrypt_cryptogram(cipheredquote, keyvalue):
    
    decryptedquote = ""

    for char in cipheredquote:
        if char.isalpha():
            is_upper = char.isupper()

            shifted = chr((ord(char) - keyvalue - ord('A' if is_upper else 'a')) % 26 + ord('A' if is_upper else 'a'))

            decryptedquote += shifted
        else:
            decryptedquote += char
    return decryptedquote

cipheredquote = input ('Enter a cryptogram: ')
keyvalue = int(input("Enter shift key value (s): "))

decipheredquote = decrypt_cryptogram(cipheredquote, keyvalue)
print("If ciphered quote is ", cipheredquote, "and 's' is ", keyvalue, "then original quote is ", decipheredquote)
