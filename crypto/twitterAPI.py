import twitter
import io

api = twitter.Api(consumer_key = 'ULhjNMU0x9QKhZ80Bv2rwg6M2',
                  consumer_secret = 'DOnEs7yRUPgdMNcnZXyEe9HcFEwaXUZWEhpW3d6UtRG49z7Bsi',
                  access_token_key = '1162030031041904640-JY4sZKv36aUF4960bgaNTsk1Hnni9m',
                  access_token_secret = 'Tv8huhZERvWCmOeJbs3sXmt9UEAADw2aOy0I7motHejur')

def getTweetIDs(name):
    lcount = 0
    with open('tweet_ids', 'r') as f:
        for line in f:
            lcount += 1
    try:
        statuses = api.GetUserTimeline(screen_name = name)
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

getTweetIDs('davethedavfadsfasdfsdafe_14')

#     pass
# uwu = api.GetUser(screen_name ='')
# print(uwu)
# statuses = api.GetUserTimeline(screen_name = '')
# wahoo = statuses[0].id
# print(wahoo)
# statoo = api.GetStatus(status_id = wahoo)
# print(statoo)
# status = api.PostUpdate('test, I\'m craving for some papaya rn')
# print(status.text)
# statuses = api.GetUserTimeline(screen_name = '')
#for s in statuses:
# print('\n%s',statuses[0].id)
# api.DestroyStatus(1247244866003832833)
# users = api.GetFriends()
# print([u.name for u in users])
# class Application(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.create_widgets()
#
#     def create_widgets(self):
#         self.hi_there = tk.Button(self)
#         self.hi_there["text"] = "Hello World\n(click me)"
#         self.hi_there["command"] = self.say_hi
#         self.hi_there.pack(side="top")
#
#         self.quit = tk.Button(self, text="QUIT", fg="red",
#                               command=self.master.destroy)
#         self.quit.pack(side="bottom")
#
#     def say_hi(self):
#         print("hi there, everyone!")
#
# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()
