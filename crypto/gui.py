import tkinter as tk
import io
import twitterAPI
import encryption

logged_in = {}
twapi = twitterAPI
crypto = encryption
key = crypto.keyRead()
user_stats = None
search_result = ''

HEIGHT = 5000
WIDTH = 5000
WIDGET_HEIGHT = 0.25
WIDGET_WIDTH = 0.25
IMG_HEIGHT = 0.075
INP_BAR = 0.1
LOGIN_BAR = IMG_HEIGHT+0.02+INP_BAR

class TwiApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(Sign_in)

    def switch_frame(self, frame_class):
            # Destroys current frame and replaces it with a new one.
            new_frame = frame_class(self)
            if self._frame is not None:
                self._frame.destroy()
            self._frame = new_frame
            #self._frame.pack()

class Sign_in(tk.Frame):
    def __init__(self, master):
        self.canvas = tk.Canvas(master, bg='white',height=HEIGHT, width=WIDTH)
        self.canvas.pack(expand=0)

        self.frame = tk.Frame(master, bg='#15202b')
        self.frame.place(relx=0,rely=0,relwidth=1,relheight=1)

        self.imageT = tk.PhotoImage(file='paras.png')
        self.image_label = tk.Label(self.frame, image=self.imageT, bg='#15202b')
        self.image_label.place(relx= 0.5-0.05 , rely = 0.02, relwidth =0.1,relheight=IMG_HEIGHT)

        self.label = tk.Label(self.frame, text='Log in señor', fg='white', bg='#15202b',font=('MS Sans Serif', 15))
        self.label.place(relx=0.5 - WIDGET_WIDTH/2, rely=IMG_HEIGHT+0.02,
                        relwidth=WIDGET_WIDTH,relheight=INP_BAR)

        self.enter = tk.Entry(self.frame, bg='#253341',fg='white',font=('MS Sans Serif',12))
        self.enter.place(relx=0.5 - WIDGET_WIDTH/2, rely=IMG_HEIGHT+0.02+INP_BAR,
                        relwidth=WIDGET_WIDTH,relheight= 0.05)

        self.hint_label = tk.Label(self.enter, text='Twitter Username', fg='#23a1f2', bg='#253341',font=('MS Sans Serif', 8))
        self.hint_label.place(relx=0, rely=0,relwidth=0.235,relheight=0.26)

        self.log_in = tk.Button(self.frame, bg='#23a1f2', fg='white', text="Log in", font=('MS Sans Serif', 12), command=lambda: self.log_in_attempt(self.enter.get(), master))
        self.log_in.place(relx=0.5 - WIDGET_WIDTH/2, rely=LOGIN_BAR+0.07,
                        relwidth=WIDGET_WIDTH, relheight=0.05)

        self.register = tk.Button(self.frame, bg='#15202b', fg='#23a1f2', text="Register account", font=('MS Sans Serif', 12), command=lambda: self.switch_sign_up(master), bd=0)
        self.register.place(relx=0.5 - WIDGET_WIDTH/2, rely=LOGIN_BAR+0.07+0.05,
                        relwidth=WIDGET_WIDTH, relheight=0.05)

    def log_in_attempt(self, input, master):

        global logged_in
        logged_in = crypto.decrypt_users(input,key)
        if logged_in == None:
            self.register.place(relx=0.5 - WIDGET_WIDTH/2, rely=LOGIN_BAR+0.07+0.05+0.05,
                            relwidth=WIDGET_WIDTH, relheight=0.05)
            self.log_in.place(relx=0.5 - WIDGET_WIDTH/2, rely=LOGIN_BAR+0.07+0.05,
                            relwidth=WIDGET_WIDTH, relheight=0.05)
            self.enter.place(relx=0.5 - WIDGET_WIDTH/2, rely=IMG_HEIGHT+0.02+INP_BAR+0.05,
                            relwidth=WIDGET_WIDTH,relheight= 0.05)
            self.warning = tk.Label(self.frame, bg='#15202b', fg='red', text="This account has not been registered", font=('MS Sans Serif', 14))
            self.warning.place(relx=0.5 - WIDGET_WIDTH/2, rely=IMG_HEIGHT+0.02+INP_BAR,
                            relwidth=WIDGET_WIDTH, relheight=0.05)
            print('youLost\n')
        else:
            print(logged_in['trust_net'])
            master.switch_frame(Home_page).pack()

    def switch_sign_up(self, master):
        master.switch_frame(Sign_up).pack()

class Sign_up(tk.Frame):
    def __init__(self, master):
        self.canvas = tk.Canvas(master, bg='white',height=HEIGHT, width=WIDTH)
        self.canvas.pack(expand=1)

        self.frame = tk.Frame(master, bg='white')
        self.frame.place(relx=0,rely=0,relwidth=1,relheight=1)

        self.frame2 = tk.Frame(self.frame, bg='white')
        self.frame2.place(relx=0.3,rely=0,relwidth=0.5,relheight=1)

        self.imageT = tk.PhotoImage(file='paras2.png')
        self.image_label = tk.Label(self.frame2, image=self.imageT, bg='white')
        self.image_label.place(relx= 0, rely = 0.005, relwidth =0.05,relheight=0.025)

        self.label3 = tk.Label(self.frame2, text='Account Registration', fg='gray', bg='white',font=('MS Sans Serif', 12))
        self.label3.place(relx=0.05, rely=0, relwidth=0.2, relheight=0.035)

        self.label = tk.Label(self.frame2, text='Find your Twitter account', fg='black', bg='white',font=('MS Sans Serif', 20))
        self.label.place(relx=0, rely=0.035, relwidth=0.32,relheight=0.1)

        self.label2 = tk.Label(self.frame2, text='Enter your Twitter username', fg='black', bg='white',font=('MS Sans Serif', 12))
        self.label2.place(relx=0, rely=0.1+0.035, relwidth=0.22,relheight=0.05)

        self.enter = tk.Entry(self.frame2, bg='white',fg='black',font=('MS Sans Serif',12),bd = 2)
        self.enter.place(relx=0.01, rely=0.185,relwidth=0.2,relheight= 0.035)

        self.search = tk.Button(self.frame2, fg='white', bg='#23a1f2',text= 'Search',
         font=('MS Sans Serif', 12),command=lambda: self.register_acc(self.enter.get(),master),bd=0)
        self.search.place(relx=0.01, rely=0.25,relwidth=0.0825,relheight= 0.035)

    def register_acc(self, u_name, master):
        global logged_in
        if twapi.legit_user(u_name):

            logged_in = {'username':u_name,
                        'pending_reqs': [],
                        'trust_net': [u_name]}
            crypto.encrypt_users(logged_in,key)
            master.switch_frame(Home_page).pack()
        else:
            self.errlabel2 = tk.Label(self.frame2, text='Please try searching for your username again.', fg='black', bg='white',font=('MS Sans Serif', 12))
            self.errlabel2.place(relx=0, rely=0.15+0.035, relwidth=0.35,relheight=0.05)
            self.errlabel = tk.Label(self.frame2, text='We couldn\'t find your account with that\n information',
            fg='red', bg='white',font=('MS Sans Serif', 22), justify='left')
            self.errlabel.place(relx=0, rely=0.035, relwidth=0.485,relheight=0.15)
            self.enter.place(relx=0.01, rely=0.235,relwidth=0.2,relheight= 0.035)
            self.search.place(relx=0.01, rely=0.235+0.065,relwidth=0.0825,relheight= 0.035)

class Home_page(tk.Frame):
    def __init__(self, master):
        self.canvas = tk.Canvas(master, bg='white',height=HEIGHT, width=WIDTH)
        self.canvas.pack(expand=1)

        self.frame_mid = tk.Frame(master, bg='#15202b', bd=3)
        self.frame_mid.place(relx=0.31,rely=0,relwidth=0.4,relheight=1)

        self.frame_left = tk.Frame(master, bg='#253341',bd=3)
        self.frame_left.place(relx=0,rely=0,relwidth=0.31,relheight=1)

        self.frame_right = tk.Frame(master, bg='#253341',bd=3)
        self.frame_right.place(relx=0.6225,rely=0,relwidth=1,relheight=1)


        self.height_inc = 0.15
        self.label_no = 0
        try:
            self.tweets_list = crypto.decrypt_tweets(logged_in['trust_net'],key)
        except TypeError:
            print('oopsie')

        for tweet in self.tweets_list:
            try:
                tweet = tweet.replace('true','True')
                tweet = eval(tweet)
                self.u_id = tweet['id']
                self.post = tweet['text']
                self.add_label_dec(self.height_inc,self.label_no, self.u_id,self.post)
            except SyntaxError as e:
                tweet = str(tweet)
                self.add_label_enc(self.height_inc,self.label_no, tweet)
            self.label_no += 1

        self.home = tk.Button(self.frame_left, bg='#253341', fg='white', text="Home", font=('MS Sans Serif', 15), command= 'On this page already')
        self.home.place(relx=0.6, rely=0.055, relwidth=0.3, relheight=0.05)
        self.profile = tk.Button(self.frame_left, bg='#253341', fg='white', text="Profile", font=('MS Sans Serif', 15), command=lambda: self.profile_switch(master))
        self.profile.place(relx=0.6, rely=0.055+0.05, relwidth=0.3, relheight=0.05)
        self.notifications = tk.Button(self.frame_left, bg='#253341', fg='white', text="Notifications", font=('MS Sans Serif', 15), command=lambda: self.notifications_switch(master))
        self.notifications.place(relx=0.6, rely=0.155, relwidth=0.3, relheight=0.05)

        self.enter = tk.Entry(self.frame_right, bg='#253341',fg='white',font=('MS Sans Serif',12))
        self.enter.place(relx=0.01, rely=0.005, relwidth=0.1,relheight= 0.05)
        self.search = tk.Button(self.frame_right, fg='white', bg='#23a1f2',text= 'Search',
         font=('MS Sans Serif', 12),command=lambda: self.search_user(self.enter.get(),master),bd=0)
        self.search.place(relx=0.01, rely=0.057,relwidth=0.1,relheight= 0.025)


    def search_user(self, input, master):
        global search_result
        user_stats = crypto.decrypt_users(input,key)
        if user_stats != None:
            search_result = input
            master.switch_frame(User_page).pack()
        else:
            print('get rick rolled')

    # adds a decrypted label
    def add_label_dec(self,height_inc, label_no, user, post):
        self.l = tk.Label(self.frame_mid,bg='#15202b',bd=3,text= str(user)+'\n'+post, fg='white',font=('MS Sans Serif', 10))
        self.l.place(relx=0, rely=0.1+(height_inc*label_no), relwidth=0.6,relheight=0.1)

    # adds an encrypted label
    def add_label_enc(self,height_inc, label_no, text):
        self.l = tk.Label(self.frame_mid,bg='#15202b',bd=3,text= 'UNKNOWN\n'+text, fg='white',font=('MS Sans Serif', 10))
        self.l.place(relx=0, rely=0.1+(height_inc*label_no), relwidth=0.6,relheight=0.1)

    def home_switch(self,master):
        print('Already on this page')

    def profile_switch(self,master):
        master.switch_frame(Network_page).pack()

    def notifications_switch(self,master):
        master.switch_frame(Notifications_page).pack()

class User_page(tk.Frame):
    def __init__(self, master):
        self.canvas = tk.Canvas(master, bg='white',height=HEIGHT, width=WIDTH)
        self.canvas.pack(expand=1)
        self.is_add = True # add or remove button

        self.frame_mid = tk.Frame(master, bg='#15202b', bd=3)
        self.frame_mid.place(relx=0.31,rely=0,relwidth=0.4,relheight=1)

        self.frame_left = tk.Frame(master, bg='#253341',bd=3)
        self.frame_left.place(relx=0,rely=0,relwidth=0.31,relheight=1)

        self.frame_right = tk.Frame(master, bg='#253341',bd=3)
        self.frame_right.place(relx=0.6225,rely=0,relwidth=1,relheight=1)

        self.label = tk.Label(self.frame_mid,bg='#15202b',bd=3,text= search_result, fg='white',font=('MS Sans Serif', 18))
        self.label.place(relx=0.02, rely=0.1, relwidth=0.35,relheight=0.1)
        self.add = tk.Button(self.frame_mid, bg='#253341', fg='white', text="Add", font=('MS Sans Serif', 12), command=lambda: self.add_to_net(master))
        self.add.place(relx=0.02, rely=0.2, relwidth=0.2, relheight=0.05)

        self.home = tk.Button(self.frame_left, bg='#253341', fg='white', text="Home", font=('MS Sans Serif', 15), command=lambda: self.home_switch(master))
        self.home.place(relx=0.6, rely=0.055, relwidth=0.3, relheight=0.05)
        self.profile = tk.Button(self.frame_left, bg='#253341', fg='white', text="Profile", font=('MS Sans Serif', 15), command=lambda: self.profile_switch(master))
        self.profile.place(relx=0.6, rely=0.055+0.05, relwidth=0.3, relheight=0.05)
        self.notifications = tk.Button(self.frame_left, bg='#253341', fg='white', text="Notifications", font=('MS Sans Serif', 15), command=lambda: self.notifications_switch(master))
        self.notifications.place(relx=0.6, rely=0.155, relwidth=0.3, relheight=0.05)

        self.enter = tk.Entry(self.frame_right, bg='#253341',fg='white',font=('MS Sans Serif',12))
        self.enter.place(relx=0.01, rely=0.005, relwidth=0.1,relheight= 0.05)
        self.search = tk.Button(self.frame_right, fg='white', bg='#23a1f2',text= 'Search',
         font=('MS Sans Serif', 12),command=lambda: self.search_user(self.enter.get(),master),bd=0)
        self.search.place(relx=0.01, rely=0.057,relwidth=0.1,relheight= 0.025)

    def search_user(self, input, master):
        global search_result
        user_stats = crypto.decrypt_users(input,key)
        if user_stats != None:
            search_result = input
            master.switch_frame(User_page).pack()
        else:
            print('get rick rolled')

    def home_switch(self,master):
        global logged_in
        logged_in = crypto.decrypt_users(logged_in['username'],key)
        master.switch_frame(Home_page).pack()

    def profile_switch(self,master):
        master.switch_frame(Network_page).pack()

    def notifications_switch(self,master):
        master.switch_frame(Notifications_page).pack()

    def add_to_net(self, master):
        popup = tk.Tk()
        popup.wm_title("!")
        label = tk.Label(popup,bd=3,text='Sent network request to '+search_result,fg='black',
        font=('MS Sans Serif', 10))
        label.pack(side="top", pady=10)
        B1 = tk.Button(popup, text="Okay", command = popup.destroy, font=('MS Sans Serif', 10),bg = 'white')
        B1.pack(side='bottom')
        if self.is_add:
            self.add.config(text='Remove', command=lambda: self.remove_from_net(master))
            self.is_add = False
        users_mod = crypto.decrypt_users(search_result,key)
        users_mod['pending_reqs'].append(logged_in['username'])
        crypto.encrypt_users(users_mod,key)
        popup.mainloop()

    def remove_from_net(self, master):
        global logged_in
        popup = tk.Tk()
        popup.wm_title("!")
        label = tk.Label(popup,bd=3,text='kamilprz has been removed from your network',fg='black',
        font=('MS Sans Serif', 10))
        label.pack(side="top", pady=10)
        B1 = tk.Button(popup, text="Okay", command = popup.destroy, font=('MS Sans Serif', 10),bg = 'white')
        B1.pack(side='bottom')
        if self.is_add == False:
            self.add.config(text='Add', command=lambda: self.add_to_net(master))
            self.is_add = True

        users_mod = crypto.decrypt_users(search_result,key)
        if logged_in['username'] in users_mod['pending_reqs']:
            users_mod['pending_reqs'].remove(logged_in['username'])
            crypto.encrypt_users(users_mod,key)
        else:
            users_mod['trust_net'].remove(logged_in['username'])
            crypto.encrypt_users(users_mod,key)
        popup.mainloop()

class Network_page(tk.Frame):
    def __init__(self, master):
        self.canvas = tk.Canvas(master, bg='white',height=HEIGHT, width=WIDTH)
        self.canvas.pack(expand=1)
        self.is_add = True # add or remove button

        self.frame_mid = tk.Frame(master, bg='#15202b', bd=3)
        self.frame_mid.place(relx=0.31,rely=0,relwidth=0.4,relheight=1)

        self.frame_left = tk.Frame(master, bg='#253341',bd=3)
        self.frame_left.place(relx=0,rely=0,relwidth=0.31,relheight=1)

        self.frame_right = tk.Frame(master, bg='#253341',bd=3)
        self.frame_right.place(relx=0.6225,rely=0,relwidth=1,relheight=1)

        global logged_in
        self.loop_count = 0
        self.height_inc = 0.15
        for user in logged_in['trust_net']:
            if user == logged_in['username'] and len(logged_in['trust_net']) == 1 :
                self.label = tk.Label(self.frame_mid,bg='#15202b',bd=3,text= 'No friends yet', fg='white',font=('MS Sans Serif', 18))
                self.label.place(relx=0.02, rely=0.1, relwidth=0.35,relheight=0.1)
            else:
                self.add_label(master,self.height_inc, self.loop_count, user)
                self.loop_count+=1

        self.home = tk.Button(self.frame_left, bg='#253341', fg='white', text="Home", font=('MS Sans Serif', 15), command=lambda: self.home_switch(master))
        self.home.place(relx=0.6, rely=0.055, relwidth=0.3, relheight=0.05)
        self.profile = tk.Button(self.frame_left, bg='#253341', fg='white', text="Profile", font=('MS Sans Serif', 15), command='On this page already')
        self.profile.place(relx=0.6, rely=0.055+0.05, relwidth=0.3, relheight=0.05)
        self.notifications = tk.Button(self.frame_left, bg='#253341', fg='white', text="Notifications", font=('MS Sans Serif', 15), command=lambda: self.notifications_switch(master))
        self.notifications.place(relx=0.6, rely=0.155, relwidth=0.3, relheight=0.05)

        self.enter = tk.Entry(self.frame_right, bg='#253341',fg='white',font=('MS Sans Serif',12))
        self.enter.place(relx=0.01, rely=0.005, relwidth=0.1,relheight= 0.05)
        self.search = tk.Button(self.frame_right, fg='white', bg='#23a1f2',text= 'Search',
         font=('MS Sans Serif', 12),command=lambda: self.search_user(self.enter.get(),master),bd=0)
        self.search.place(relx=0.01, rely=0.057,relwidth=0.1,relheight= 0.025)
        #self.remove_from_net(master,'kamilprz')

    def search_user(self, input, master):
        global search_result
        user_stats = crypto.decrypt_users(input,key)
        if user_stats != None:
            search_result = input
            master.switch_frame(User_page).pack()
        else:
            print('get rick rolled')

    def home_switch(self,master):

        global logged_in
        logged_in = crypto.decrypt_users(logged_in['username'],key)
        master.switch_frame(Home_page).pack()

    def profile_switch(self,master):
        print('You\'re already on this page')

    def notifications_switch(self,master):
        master.switch_frame(Notifications_page).pack()

    def remove_from_net(self, master, label, button1, u_name):
        global logged_in
        popup = tk.Tk()
        popup.wm_title("!")
        label = tk.Label(popup,bd=3,text=u_name+' has been removed from the network',fg='black',
        font=('MS Sans Serif', 10))
        label.pack(side="top", pady=10)
        B1 = tk.Button(popup, text="Okay", command = popup.destroy, font=('MS Sans Serif', 10),bg = 'white')
        B1.pack(side='bottom')
        label.destroy()
        button1.destroy()

        users_mod = crypto.decrypt_users(u_name,key)
        users_mod['trust_net'].remove(logged_in['username'])
        crypto.encrypt_users(users_mod,key)
        logged_in['trust_net'].remove(u_name)
        crypto.encrypt_users(logged_in,key)
        popup.mainloop()

    def add_label(self, master,height_inc, label_no, user):
        self.l = tk.Label(self.frame_mid,bg='#15202b',bd=3,text= user, fg='white',font=('MS Sans Serif', 18))
        self.l.place(relx=0.02, rely=0.1+(height_inc*label_no), relwidth=0.35,relheight=0.1)
        self.remove = tk.Button(self.frame_mid, bg='#253341', fg='white', text="Remove", font=('MS Sans Serif', 12))
        self.remove.place(relx=0.0, rely=0.2+(height_inc*label_no), relwidth=0.2, relheight=0.05)
        self.remove.config(command=lambda: self.remove_from_net(master,self.l,self.remove,user))

class Notifications_page(tk.Frame):
    def __init__(self, master):
        global logged_in
        self.canvas = tk.Canvas(master, bg='white',height=HEIGHT, width=WIDTH)
        self.canvas.pack(expand=1)
        self.is_add = True # add or remove button

        self.frame_mid = tk.Frame(master, bg='#15202b', bd=3)
        self.frame_mid.place(relx=0.31,rely=0,relwidth=0.4,relheight=1)

        self.frame_left = tk.Frame(master, bg='#253341',bd=3)
        self.frame_left.place(relx=0,rely=0,relwidth=0.31,relheight=1)

        self.frame_right = tk.Frame(master, bg='#253341',bd=3)
        self.frame_right.place(relx=0.6225,rely=0,relwidth=1,relheight=1)

        self.loop_count = 0
        self.height_inc = 0.15
        if logged_in['pending_reqs'] == []:
            self.label = tk.Label(self.frame_mid,bg='#15202b',bd=3,text= 'No new requests', fg='white',font=('MS Sans Serif', 18))
            self.label.place(relx=0.02, rely=0.1, relwidth=0.35,relheight=0.1)
        else:
            for request in logged_in['pending_reqs']:
                self.add_label(master,self.height_inc, self.loop_count, request)
                self.loop_count+=1

        self.home = tk.Button(self.frame_left, bg='#253341', fg='white', text="Home", font=('MS Sans Serif', 15), command=lambda: self.home_switch(master))
        self.home.place(relx=0.6, rely=0.055, relwidth=0.3, relheight=0.05)
        self.profile = tk.Button(self.frame_left, bg='#253341', fg='white', text="Profile", font=('MS Sans Serif', 15), command=lambda: self.profile_switch(master))
        self.profile.place(relx=0.6, rely=0.055+0.05, relwidth=0.3, relheight=0.05)
        self.notifications = tk.Button(self.frame_left, bg='#253341', fg='white', text="Notifications", font=('MS Sans Serif', 15), command=lambda: self.notifications_switch())
        self.notifications.place(relx=0.6, rely=0.155, relwidth=0.3, relheight=0.05)

        self.enter = tk.Entry(self.frame_right, bg='#253341',fg='white',font=('MS Sans Serif',12))
        self.enter.place(relx=0.01, rely=0.005, relwidth=0.1,relheight= 0.05)
        self.search = tk.Button(self.frame_right, fg='white', bg='#23a1f2',text= 'Search',
         font=('MS Sans Serif', 12),command=lambda: self.search_user(self.enter.get(),master),bd=0)
        self.search.place(relx=0.01, rely=0.057,relwidth=0.1,relheight= 0.025)
        #self.remove_from_net(master,'kamilprz')

    def search_user(self, input, master):
        global search_result
        user_stats = crypto.decrypt_users(input,key)
        if user_stats != None:
            search_result = input
            master.switch_frame(User_page).pack()
        else:
            print('get rick rolled')

    def home_switch(self,master):
        global logged_in

        logged_in = crypto.decrypt_users(logged_in['username'],key)
        master.switch_frame(Home_page).pack()

    def profile_switch(self,master):
        master.switch_frame(Network_page).pack()

    def notifications_switch(self):
        print('You\'re already on this page')

    # adds a label and it's remove button
    def add_label(self, master,height_inc, label_no, user):
        self.l = tk.Label(self.frame_mid,bg='#15202b',bd=3,text= user, fg='white',font=('MS Sans Serif', 18))
        self.l.place(relx=0.02, rely=0.1+(height_inc*label_no), relwidth=0.35,relheight=0.1)
        self.accept = tk.Button(self.frame_mid, bg='#253341', fg='white', text="Accept", font=('MS Sans Serif', 12))
        self.accept.place(relx=0.0, rely=0.2+(height_inc*label_no), relwidth=0.2, relheight=0.05)
        self.decline = tk.Button(self.frame_mid, bg='#253341', fg='white', text="Reject", font=('MS Sans Serif', 12))
        self.decline.place(relx=0.22, rely=0.2+(height_inc*label_no), relwidth=0.2, relheight=0.05)
        self.accept.config(command=lambda: self.accept_in(master,self.l,self.decline,self.accept, user))
        self.decline.config(command=lambda: self.decline_in(master,self.l,self.decline,self.accept,user))


    def decline_in(self, master, label,button1,button2,u_name):
        global logged_in
        popup = tk.Tk()
        popup.wm_title("!")
        label_pop_up = tk.Label(popup,bd=3,text=u_name+' has been removed from the network',fg='black',
        font=('MS Sans Serif', 10))
        label_pop_up.pack(side="top", pady=10)
        B1 = tk.Button(popup, text="Okay", command = popup.destroy, font=('MS Sans Serif', 10),bg = 'white')
        B1.pack(side='bottom')
        label.destroy()
        button2.destroy()
        button1.destroy()

        logged_in['pending_reqs'].remove(u_name)
        crypto.encrypt_users(logged_in,key)
        popup.mainloop()

    def accept_in(self, master, label,button1,button2,u_name):
        global logged_in
        popup = tk.Tk()
        popup.wm_title("!")
        label_pop_up = tk.Label(popup,bd=3,text=u_name+' has been added into the network',fg='black',
        font=('MS Sans Serif', 10))
        label_pop_up.pack(side="top", pady=10)
        B1 = tk.Button(popup, text="Okay", command = popup.destroy, font=('MS Sans Serif', 10),bg = 'white')
        B1.pack(side='bottom')
        label.destroy()
        button2.destroy()
        button1.destroy()

        users_mod = crypto.decrypt_users(u_name,key)
        users_mod['trust_net'].append(logged_in['username'])
        crypto.encrypt_users(users_mod,key)
        logged_in['pending_reqs'].remove(u_name)
        logged_in['trust_net'].append(u_name)
        crypto.encrypt_users(logged_in,key)
        popup.mainloop()

if __name__ == "__main__":
    app = TwiApp()
    app.mainloop()
