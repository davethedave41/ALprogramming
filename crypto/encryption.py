from cryptography.fernet import Fernet
import io

#Function which generates our key (AES)
def keyGen():
    key = Fernet.generate_key()
    # with open('key.key','wb') as f:
    # f.write(key)
    file = open('key.key', 'wb')
    file.write(key)
    file.close()

#Function which reads the key
def keyRead():
    try:
        # with open('key.key','rb') as f:
        # f.read()
        file = open('key.key', 'rb') # must be in binary format
        key = file.read()
        file.close()
        return key
    except FileNotFoundError:
        #If key does not exists a new one is created.
        print("No Key exists, a new one has just been created.")
        keyGen()
        keyRead()

#Function to encrypt files using the key
def encrypt(tweet, Key):
    with open('mytweets', 'rb') as f:
        tweet = f.read()
    return tweet
#    fernet = Fernet(Key)
    #encrypted = fernet.encrypt(data)
#    with open("Files/"+ fileName, "wb") as f:
#        f.write(tweet)

#Function to decrypt files using the key
def decrypt(tweet, Key):
    fernet = Fernet(Key)
    # get the tweet using api
    decrypted = fernet.decrypt(data)
