

def decryption(ct):
    msg = ""
    for index in range(0, len(ct), 2):
        char_int = int(ct[index:index+2], 16)
        for i in range(256):
            x = (char_int + (i*256) - 18 ) / 123
            if x.is_integer():
                msg += chr(int(x))
                break
    return msg

# Usage
with open('./msg.enc', 'rb') as f:
    string = f.read()

plain_text = decryption(string)
print(plain_text)
