import rsa
'''
with open('bababooeyPub.pem', mode='rb') as f:
    keyData = f.read()
    print(keyData)
publicKey = rsa.PublicKey.load_pkcs1_openssl_pem(keyData)

print(publicKey)
'''

with open('bababooeyPub.pem', mode='rb') as f:
    keyData = f.read()
    print(keyData)
publicKey = rsa.PublicKey.load_pkcs1_openssl_pem(keyData)

print(publicKey)
