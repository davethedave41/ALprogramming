import twitter
import tkinter as tk

api = twitter.Api(consumer_key = '',
                  consumer_secret = '',
                  access_token_key = '',
                  access_token_secret = '',
                  sleep_on_rate_limit = True)

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
