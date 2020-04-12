import twitter
import io
import encryption
import sys

crypto = encryption
api = twitter.Api(consumer_key = 'ULhjNMU0x9QKhZ80Bv2rwg6M2',
                  consumer_secret = 'DOnEs7yRUPgdMNcnZXyEe9HcFEwaXUZWEhpW3d6UtRG49z7Bsi',
                  access_token_key = '1162030031041904640-JY4sZKv36aUF4960bgaNTsk1Hnni9m',
                  access_token_secret = 'Tv8huhZERvWCmOeJbs3sXmt9UEAADw2aOy0I7motHejur')

# is this a twitter username
def legit_user(u_name):
    try:
        getTimeline = api.GetUserTimeline(screen_name = u_name)
    except twitter.error.TwitterError as e:
        error_str = str(e)
        #error_str = error_str[26:58]
        #print(error_str)
        return False
    return True

# read from twitter
def getTweets(u_name):
    tweets = api.GetUserTimeline(screen_name = u_name)
    key = crypto.keyRead()
    for post in tweets:
        post = str(post)
        post = post.replace('true','True')
        crypto.encrypt_tweets(post,u_name,key)

# getting from file
def readTweets(trust_net):
    # returns a list of the encrypted and decrypted tweets'
    key = crypto.keyRead()
    listOfTweets = crypto.decrypt_tweets(trust_net, key)
    return listOfTweets

u_name = 'davethedave_14'
getTweets(u_name)
readTweets(u_name)
awooga = readTweets([u_name])
awoogerz = eval(awooga[0])
print(awoogerz['id'])
