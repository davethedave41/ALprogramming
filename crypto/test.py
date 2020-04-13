import tkinter as tk

root = tk.Tk()
# sb = tk.Scrollbar(root, bg='yellow',activebackground='red')
# sb.pack(side = 'right', fill = 'y')
#
# mylist = tk.Listbox(root, yscrollcommand = sb.set )
#
# for line in range(30):
#     mylist.insert('end', "Number " + str(line))
#
# mylist.pack( side = 'left' )
# sb.config( command = mylist.yview )
#
# root.mainloop()
def motion(event):
  print("Mouse position: (%s %s)" % (event.x, event.y))
  return

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = tk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
msg = tk.Message(root, text = whatever_you_do)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.bind('<Motion>',popupmsg('wait you have boobs'))
msg.pack()
root.mainloop()
