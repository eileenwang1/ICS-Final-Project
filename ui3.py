from tkinter import *
import tkinter.messagebox

from chat_client_class import *


def main():
    import argparse
    parser = argparse.ArgumentParser(description='chat client argument')
    parser.add_argument('-d', type=str, default=None, help='server IP addr')
    args = parser.parse_args()

    client = Client(args)
    c_ui3 = GUI3(client)

    #todo: put it in ui
    #client.run_chat()





class GUI3:
    def __init__(self, client):
        #self.system_msg = ''
        self.client = client

        self.root = Tk(className='Welcome to ICS chat')
        self.frame_1 = Frame(self.root)
        self.frame_2 = Frame(self.root)
        self.frame_3 = Frame(self.root)

        self.scroll = Scrollbar(self.frame_1)
        self.scroll.pack(side=RIGHT, fill=Y)
        #self.menu = menu.split("\n")
        # self.menu is a list of the string
        self.listbox = Listbox(self.frame_1, yscrollcommand=self.scroll.set, width=500)

        #for i in self.menu:
            #self.listbox.insert(END, str(i))
        self.listbox.insert(END, "Please enter your name")
        self.listbox.pack(side=LEFT)

        self.scroll.config(command=self.listbox.yview)
        self.frame_1.pack()

        self.button1 = Button(self.frame_2, text='Send', command=self.send)
        self.to_send = ""

        self.button1.pack(side=LEFT)
        self.frame_2.pack()

        self.prompt_label = Label(self.frame_3, text='enter below')
        self.entry = Entry(self.frame_3, width=70)

        self.prompt_label.pack(side=TOP)
        self.entry.pack(side=TOP)

        self.frame_3.pack()

        self.root.geometry("500x500")
        self.root.mainloop()

        #please enter your name
#new ui, all in one

#copy the chat_client_class

#the magical send button

#log_in, display name

    def send(self):
        message = self.entry.get()
        if len(message) == 0:
            tkinter.messagebox.showinfo("Warning", "Can't sent empty message!")
        else:
            self.listbox.insert(END, message)   #insert into the dialogue box
                                                #how to pass it to the server?

            self.entry.delete(0, END)           #delete was sended to the message box
            self.to_send = message

        #self.frame.pack()
        '''
        my_msg = self.to_send
        peer_msg = ''
        self.system_msg += self.sm.proc(my_msg, peer_msg)
        self.to_send = ''
        '''

#determine state (time, who, connect, gameing)
if __name__ == '__main__':

    main()