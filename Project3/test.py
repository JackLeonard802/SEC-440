import rsa

with open('bababooey.pem', mode='rb') as privatefile:
    keydata = privatefile.read()
    print(keydata)
privkey = rsa.PrivateKey.load_pkcs1(keydata)

print(privkey)
'''

with open('bababooeyPub.pem', mode='rb') as f:
    keyData = f.read()
    print(keyData)
publicKey = rsa.PublicKey.load_pkcs1_openssl_pem(keyData)

print(publicKey)
'''