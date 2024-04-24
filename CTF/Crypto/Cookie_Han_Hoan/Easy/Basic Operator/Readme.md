# Basic Operator

## a challenge in `Cookie Han Hoan` about apply mathematic computation to solve. We look at the code to see how it work.

```python
import math

from Crypto.Util import number

def padding_pkcs7(data,block_size=4):
	tmp = len(data) + (block_size - len(data) % block_size)
	print("pad")
	print(data.ljust(tmp,bytes([block_size-(len(data)%block_size)])))
	return data.ljust(tmp,bytes([block_size-(len(data)%block_size)]))

def split_block(data,block_size):
	print("split")
	print(list(int.from_bytes(data[i:i+block_size],'little') for i in range(0,len(data),block_size)))
	return list(int.from_bytes(data[i:i+block_size],'little') for i in range(0,len(data),block_size))

def plus_func(data,shift):
	print("plus")
	print((data+shift)&0xffffffff)
	return (data+shift)&0xffffffff

def mul_func(data,mul):
	print("mul")
	print((data*mul)&0xffffffff)
	return (data*mul)&0xffffffff

def xor_shift_right_func(data,bit_loc):
	print("xor")
	print((data^(data>>bit_loc))&0xffffffff)
	return (data^(data>>bit_loc))&0xffffffff

def pow_func(data,e,p):
	print("pow")
	print(pow(data,e,p))
	return pow(data,e,p)

def exp_func(data,base,p):
	print("exp")
	print(pow(base,data,p))
	return pow(base,data,p)

def ecb_mode(data):
	return list(pow_func(exp_func(xor_shift_right_func(mul_func(plus_func(block,3442055609),2898124289),1),e,p),e,p) for block in split_block(padding_pkcs7(data,4),4))

if __name__=='__main__':
	p = 1341161101353773850779
	e = 2
	mess = b'CHH{w3lc0m3_70_7h3_m47h_w0rld(1_h4t3_1t_th3r3)}'
	cipher_flag = ecb_mode(mess)
	print(cipher_flag)
```
