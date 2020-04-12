import twitter
import io
import encryption
import sys

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

def getTweets(u_name):
    lcount = 0
    with open('tweet_ids', 'r') as f:
        for line in f:
            lcount += 1
    statuses = api.GetUserTimeline(screen_name = u_name)
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

def readTweets():
    with open('tweets', 'r') as f:
        tweet = f.read()
    return tweet

stats = api.GetUserTimeline(screen_name='davethedave_14')
stat_str = str(stats[0])+'\n'
stat_true = stat_str.replace("true","True")
file = open('tweets.txt','a')
file.write(stat_true)
stat_dict = eval(stat_true)
file = open('tweets.txt','r')
for i, line in enumerate(file):
    if i == 1:
        datum = line
print(datum)
file.close()
