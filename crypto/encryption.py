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
    u_data = {'username': u_name,
              'trust_net': [],
              'pending_reqs': []}
    u_data = str(u_data)
    u_data += '\n'
    fernet = Fernet(Key)
    encrypted = fernet.encrypt(u_data.encode())
    with open('users.txt','ab') as f:
        f.write(encrypted)

# ecnrypts a single tweet
def encrypt_tweets(tweet, u_name, Key):
    wahoo = u_name+'\n'
    tweet+=wahoo
    fernet = Fernet(Key)
    encrypted = fernet.encrypt(tweet.encode())
    with open('tweets.txt','ab') as f:
        f.write(encrypted)

# decrypts tweets ONLY if user is in the trust network
# returns a list of strings, decrypted posts must be converted to dictionaries
def decrypt_tweets(trust_net, Key):
    trusted = False
    tweets = []
    fernet = Fernet(Key)
    with open('tweets.txt','rb') as f:
        for line in f:
            decrypted = fernet.decrypt(line)
            decrypted = decrypted.decode()
            for name in trust_net:
                if name+'\n' in decrypted:
                    decrypted = decrypted.replace(name+'\n', '')
                    tweets.append(decrypted)
                    trusted = True
                    break
            if trusted == True:
                pass
            else:
                tweets.append(line)

    print('victory royale')
    return tweets

# decrypt usernames using the key
def decrypt_users(u_name, Key):
    fernet = Fernet(Key)
    with open('users.txt','rb') as f:
        for line in f:
            decrypted = fernet.decrypt(line)
            decrypted = decrypted.decode()
            decrypted = decrypted.replace('\n', '')
            decrypted = eval(decrypted)
            if decrypted['username'] == u_name:
                print('victory royale')
                return decrypted
    print('sorry homie')
