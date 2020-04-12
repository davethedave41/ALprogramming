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

# Function to encrypt usernames using the key
def encrypt_users(u_name, Key):
    u_name += '\n'
    fernet = Fernet(Key)
    encrypted = fernet.encrypt(u_name.encode())
    with open('users.txt','ab') as f:
        f.write(encrypted)

# ecnrypt userbase tweets using the key
def encrypt_tweets(tweet, Key):
    tweet += '\n'
    fernet = Fernet(Key)
    encrypted = fernet.encrypt(u_name.encode())
    with open('tweet_ids.txt','ab') as f:
        f.write(encrypted)

#Function to decrypt userbase tweets using the key
def decrypt_tweets(tweet, Key):
    fernet = Fernet(Key)
    with open('tweet_ids.txt','rb') as f:
        for line in f:
            decrypted = fernet.decrypt(line)
            decrypted = decrypted.decode()
            decrypted = decrypted.replace('\n', '')
            if decrypted =='u_name':
                print('victory royale')
                return decrypted
    print('sorry homie')

# decrypt usernames using the key
def decrypt_users(u_name, Key):
    fernet = Fernet(Key)
    with open('users.txt','rb') as f:
        for line in f:
            decrypted = fernet.decrypt(line)
            decrypted = decrypted.decode()
            decrypted = decrypted.replace('\n', '')
            if decrypted == u_name:
                print('victory royale')
                return decrypted
    print('sorry homie')
