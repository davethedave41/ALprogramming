import tkinter as tk
import io
import twitterAPI
import encryption

twapi = twitterAPI
crypto = encryption
key = crypto.keyRead()

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
        self.switch_frame(Sign_up)

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
        waha = 'D'
        print('nice')
        # with open('users.txt', 'r') as f:
        #     for line in f:
        #         if line == input:
        if(waha == input):
            print('hah gay\n')
            master.switch_frame(User_menu).pack()
        else:
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
        if twapi.legit_user(u_name):
            u_name += '\n'
            key = crypto.keyRead()
            fernet = crypto.Fernet(key)
            encrypted = fernet.encrypt(u_name.encode())
            with open('users.txt','ab') as f:
                f.write(encrypted)
            master.switch_frame(User_menu).pack()
        else:
            self.errlabel2 = tk.Label(self.frame2, text='Please try searching for your username again.', fg='black', bg='white',font=('MS Sans Serif', 12))
            self.errlabel2.place(relx=0, rely=0.15+0.035, relwidth=0.35,relheight=0.05)
            self.errlabel = tk.Label(self.frame2, text='We couldn\'t find your account with that\n information',
            fg='red', bg='white',font=('MS Sans Serif', 22), justify='left')
            self.errlabel.place(relx=0, rely=0.035, relwidth=0.485,relheight=0.15)
            self.enter.place(relx=0.01, rely=0.235,relwidth=0.2,relheight= 0.035)
            self.search.place(relx=0.01, rely=0.235+0.065,relwidth=0.0825,relheight= 0.035)

class User_menu(tk.Frame):
    def __init__(self, master):
        self.canvas = tk.Canvas(master, bg='white',height=HEIGHT, width=WIDTH)
        self.canvas.pack(expand=1)

        self.frame = tk.Frame(master, bg='#15202b')
        self.frame.place(relx=0,rely=0,relwidth=1,relheight=1)

        self.imageT = tk.PhotoImage(file='paras.png')
        self.image_label = tk.Label(self.frame, image=self.imageT, bg='#15202b')
        self.image_label.place(relx= 0.5-0.05 , rely = 0.02, relwidth =0.1,relheight=IMG_HEIGHT)

        self.label = tk.Label(self.frame, text='Log in to wahoo señor', fg='white', bg='#15202b',font=('MS Sans Serif', 15))
        self.label.place(relx=0.5 - WIDGET_WIDTH/2, rely=IMG_HEIGHT+0.02,
                         relwidth=WIDGET_WIDTH,relheight=INP_BAR)

        self.enter = tk.Entry(self.frame, bg='#253341',fg='white',font=('MS Sans Serif',12))
        self.enter.place(relx=0.5 - WIDGET_WIDTH/2, rely=IMG_HEIGHT+0.02+INP_BAR,
                         relwidth=WIDGET_WIDTH,relheight= 0.05)

        self.hint_label = tk.Label(self.enter, text='Twitter Username', fg='#23a1f2', bg='#253341',font=('MS Sans Serif', 8))
        self.hint_label.place(relx=0, rely=0,relwidth=0.235,relheight=0.26)

        self.log_in = tk.Button(self.frame, bg='#23a1f2', fg='white', text="Log in", font=('MS Sans Serif', 12), command= 'hello cuck')
        self.log_in.place(relx=0.5 - WIDGET_WIDTH/2, rely=LOGIN_BAR+0.07,
                         relwidth=WIDGET_WIDTH, relheight=0.05)


if __name__ == "__main__":
    app = TwiApp()
    app.mainloop()
