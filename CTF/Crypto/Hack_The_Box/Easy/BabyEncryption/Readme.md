# BabyEncryption - Hack_The_Box

## These challenge provide a simple encryption with a kind of Substitution Cipher

![image](https://github.com/Ov3rxn4ght-Projects/Trong-Tinh/assets/107429242/9e482081-235d-4947-baf8-68ca79e5f103)

### The Encryption Algorithms take each of the character x in plain text then ( 123*char + 18 ) % 256

### to solve this we can break down the Algorithms like:
    cipher = ( 123*char + 18 )  % 256
    cipher + (k*256) = 123*char + 18
    cipher + (k*256) - 18 / 123
> \{x}{y}
