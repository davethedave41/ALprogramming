import tkinter as tk
import io

HEIGHT = 5000
WIDTH = 5000

WIDGET_HEIGHT = 0.25
WIDGET_WIDTH = 0.25
IMG_HEIGHT = 0.075
INP_BAR = 0.1
LOGIN_BAR = IMG_HEIGHT+0.02+INP_BAR

sign_in = tk.Tk()


canvas = tk.Canvas(sign_in, bg='#15202b',height=HEIGHT, width=WIDTH)
canvas.pack(expand=1)

frame = tk.Frame(sign_in, bg='#15202b')
frame.place(relx=0.1,rely=0,relwidth=0.8,relheight=0.8)

imageT = tk.PhotoImage(file='tweet.png')
image_label = tk.Label(frame, image=imageT, bg='#15202b')
image_label.place(relx= 0.5-0.05 , rely = 0.02, relwidth =0.1,relheight=IMG_HEIGHT)

label = tk.Label(frame, text='Log in to Tweeter señor', fg='white', bg='#15202b',font=('MS Sans Serif', 15))
label.place(relx=0.5 - WIDGET_WIDTH/2, rely=IMG_HEIGHT+0.02,
                relwidth=WIDGET_WIDTH,relheight=INP_BAR)

enter = tk.Entry(frame, bg='#253341',fg='white',font=('MS Sans Serif',12))
enter.place(relx=0.5 - WIDGET_WIDTH/2, rely=IMG_HEIGHT+0.02+INP_BAR,
                relwidth=WIDGET_WIDTH,relheight= 0.05)

hint_label = tk.Label(enter, text='Twitter Username', fg='#23a1f2', bg='#253341',font=('MS Sans Serif', 8))
hint_label.place(relx=0, rely=0,relwidth=0.235,relheight=0.26)

log_in = tk.Button(frame, bg='#23a1f2', fg='white', text="Log in", font=('MS Sans Serif', 12),
                      command=sign_in.destroy)
log_in.place(relx=0.5 - WIDGET_WIDTH/2, rely=LOGIN_BAR+0.07,
                relwidth=WIDGET_WIDTH, relheight=0.05)
# log_in.grid(row=0, column=2)

def log_in_attempt(input):
    with open('users.txt')

sign_in.mainloop()
