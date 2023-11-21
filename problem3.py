

def caesar_encrypt(key, message):
    """Encrypt a message"""
    encrypted_message = ""
    for i in message: 
        if i.isalpha():
            upper = i.isupper()
            alpha = i.upper()
            alpha_code = ord(alpha)

            encrypted_ord = ((alpha_code - 65 + key) % 26) + 65
            if not upper: 
                encrypted_ord = encrypted_ord + 32
                
            encrypted_message = encrypted_message + chr(encrypted_ord )
        else:
             encrypted_message = encrypted_message + i
    
    return encrypted_message


def caesar_decrypt(key, message):
    """Decrypt a message"""
    decrypted_message  = ""
    for i in message: 
        if i.isalpha():
            upper = i.isupper()
            alpha = i.upper()
            alpha_code = ord(alpha)

            decrypted_ord = ((alpha_code - 65 + key) % 26) + 65
            if not upper: 
                decrypted_ord = decrypted_ord + 32
               
            decrypted_message  = decrypted_message  + chr( decrypted_ord)
        else:
             decrypted_message  = decrypted_message  + i
    return decrypted_message


key = 12
message = "Experience is the teacher of all things."

encrypted_quote = caesar_encrypt(key, message)
print(encrypted_quote)

decrypted_quote = caesar_decrypt(key, encrypted_quote)
print(decrypted_quote)