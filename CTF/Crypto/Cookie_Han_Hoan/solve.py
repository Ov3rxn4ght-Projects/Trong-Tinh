from Crypto.Util.number import bytes_to_long, long_to_bytes
from sympy.ntheory import discrete_log

def rev_pow_func(result, p):
    root1 = pow(result, (p + 1) // 4, p)
    root2 = p - root1
    return root1, root2


def rev_exp_func(ouput, base, p):
    return discrete_log(p, ouput, base)


def rev_xor_func(y):
    x = y
    for i in range(1000):
        if x ^ (x>>1) & 0xffffffff == y:
            return x
        x = x ^ (x>>1)

    return -1

def rev_mul_func(k):
    ori = k
    for i in range(2**32):
        x = (k * 2898124289) & 0xffffffff
        if (x * 2898124289 & 0xffffffff) == ori:
            return (x)
        k = (k * 2898124289) & 0xffffffff

    return None

def rev_plus_func(y):
    return (y - 3442055609) & 0xffffffff


def rev_split_little(y):
    return (long_to_bytes(y).decode())[::-1]


p = 1341161101353773850779
e = 2
cipher = [752589857254588976778, 854606763225554935934, 102518422244000685572, 779286449062901931327, 424602910997772742508, 1194307203769437983433, 501056821915021871618, 691835640758326884371, 778501969928317687301, 1260460302610253211574, 833211399330573153864, 223847974292916916557]
answer = ""
for ouput in cipher:
    if rev_xor_func(rev_exp_func(rev_pow_func(ouput, p)[0], e, p)) != -1:
        #answer += (rev_split_little(rev_plus_func(rev_mul_func(rev_xor_func(rev_exp_func(rev_pow_func(ouput, p)[0], e, p))))))
        answer += (rev_split_little(rev_plus_func(rev_mul_func(rev_xor_func(rev_exp_func(rev_pow_func(ouput, p)[0], e, p))))))
    else:
        #answer += (rev_split_little(rev_plus_func(rev_mul_func(rev_xor_func(rev_exp_func(rev_pow_func(ouput, p)[1], e, p))))))
        answer += (rev_split_little(rev_plus_func(rev_mul_func(rev_xor_func(rev_exp_func(rev_pow_func(ouput, p)[1], e, p))))))
    print(answer)


