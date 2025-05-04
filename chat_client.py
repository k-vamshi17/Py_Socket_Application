import socket
import tkinter as tk
import threading
from tkinter import scrolledtext

class ChatClient:
    def __init__(self,master,host="localhost",port=5555):
        self.master=master
        self.master.title("ChatClient")
        self.chat_area=scrolledtext.ScrolledText(master,state='disabled',width=50,
                                                 height=20)
        self.chat_area.pack(padx=10,pady=10)
        self.entry_msg=tk.Entry(master,width=40)
        self.entry_msg.pack(side=tk.LEFT)
        self.send_button=tk.Button(master,text="Send",command=self.send_message)
        self.send_button.pack(side=tk.LEFT)
        self.client=socket.socket()
        self.client.connect((host,port))
        thread=threading.Thread(target=self.receive_message,daemon=True)
        thread.start()
    def send_message(self):
        msg=self.entry_msg.get()
        self.client.send(msg.encode())
        self.display_message("You",msg)
        self.entry_msg.delete(0,tk.END)
    def receive_message(self):
        while True:
            msg=self.client.recv(1024)
            msg=msg.decode()
            self.display_message("Friend",msg)
    def display_message(self,sender,msg):
        self.chat_area.config(state="normal")
        self.chat_area.insert(tk.END,f'{sender}:{msg}\n')
        self.chat_area.config(state="disable")
        

root=tk.Tk()
client=ChatClient(root)
root.mainloop()
