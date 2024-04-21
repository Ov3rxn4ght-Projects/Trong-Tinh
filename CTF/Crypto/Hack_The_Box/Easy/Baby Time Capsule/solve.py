
from pydoc import plain
from Crypto.Util.number import long_to_bytes
from pwn import *
from sympy.functions.combinatorial.numbers import nT
from sympy.ntheory.modular import crt
from sympy.simplify.simplify import nthroot

connect = remote('94.237.62.149', 39050)

remainder = list()
modulus = list()

for i in range(3):
    connect.sendline(b'Y')
    a = connect.recvline().decode()
    arr = a.split('"')
    print(arr)
    remainder.append(int(arr[3], 16))
    modulus.append(int(arr[7], 16))


m = crt(modulus, remainder)
root_5 = nthroot(m[0], 5)
print(int(root_5))
plain_text = long_to_bytes(int(root_5))
print(plain_text)

connect.sendline(b'N')
connect.recvline()
connect.close()