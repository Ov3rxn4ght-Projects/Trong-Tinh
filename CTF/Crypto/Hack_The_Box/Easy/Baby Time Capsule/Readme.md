# Baby Time Capsule

## Look a bits about the code here [server.py](server.py):

![image](https://github.com/Ov3rxn4ght-Projects/Trong-Tinh/assets/107429242/2d0ac454-c64e-4209-9442-1ce89b8de477)

### we can see that the `_get_new_pubkey` generate random value of `n` and a same value 5 for `e`. Then, it take the the `flag` to encrypt with the modular exponent.
### then it return the cipher-text `m`, `n` and `e`.

![image](https://github.com/Ov3rxn4ght-Projects/Trong-Tinh/assets/107429242/a82bd0c2-ae53-4298-bd18-7d4f158959d8)

### as the code provide here and the image below, everytime we sumbit `Y` to the server it then generate a new `n`, new cipher-text `m` and a same `e` here.

![image](https://github.com/Ov3rxn4ght-Projects/Trong-Tinh/assets/107429242/0e9577eb-15d8-4677-b480-a5f82207af1a)


With the same `e` everytime and new `n` and `m` we can form this:


