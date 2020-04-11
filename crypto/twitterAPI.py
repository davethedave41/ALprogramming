import twitter
import io
import encryption

api = twitter.Api(consumer_key = 'ULhjNMU0x9QKhZ80Bv2rwg6M2',
                  consumer_secret = 'DOnEs7yRUPgdMNcnZXyEe9HcFEwaXUZWEhpW3d6UtRG49z7Bsi',
                  access_token_key = '1162030031041904640-JY4sZKv36aUF4960bgaNTsk1Hnni9m',
                  access_token_secret = 'Tv8huhZERvWCmOeJbs3sXmt9UEAADw2aOy0I7motHejur')

def legit_user(u_name):
    try:
        getTimeline = api.GetUserTimeline(screen_name = u_name)
    except twitter.error.TwitterError as e:
        error_str = str(e)
        #error_str = error_str[26:58]
        #print(error_str)
        return False
    return True
def getTweetIDs(u_name):
    lcount = 0
    with open('tweet_ids', 'r') as f:
        for line in f:
            lcount += 1
    try:
        statuses = api.GetUserTimeline(screen_name = u_name)
    except twitter.error.TwitterError as e:
        error_str = str(e)
        print(error_str[26:58])
        print('\nawooga')
        return
    ids_count = len(statuses)
    if ids_count == lcount and ids_count != 0:
        print('File is up to date\n')
        return
    else:
        f = open('tweet_ids', 'a')
        starti = lcount-1                   # starting index
        for i in range(starti,ids_count):
            tweet_id = str(statuses[i].id)+'\n'
            f.write(tweet_id)
            print(tweet_id)    # FIFO
        f.close()

#[{'code': 34, 'message': 'Sorry, that page does not exist.'}]
def readTweetIDs():
    with open('tweet_ids', 'r') as f:
        tweet = f.read()
    return tweet
#string formatting

crypto = encryption
key = crypto.keyRead()
fernet = crypto.Fernet(key)
with open('users.txt','rb') as f:
    for line in f:
        decrypted = fernet.decrypt(line)
        decrypted = decrypted.decode()
        decrypted = decrypted.replace('\n', '')
        if decrypted =='davethedave_14':
            print('victory royale')
