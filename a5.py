import tkinter as tk
from tkinter import ttk, filedialog
from typing import Text
import ds_messenger
from Profile import Profile
from LastFM import LastFM
from OpenWeather import OpenWeather


class Body(tk.Frame):
    def __init__(self, root, recipient_selected_callback=None):
        tk.Frame.__init__(self, root)
        self.root = root
        self._contacts = [str]
        self._select_callback = recipient_selected_callback
        # After all initialization is complete,
        # call the _draw method to pack the widgets
        # into the Body instance
        self._draw()

    def node_select(self, event):
        index = int(self.posts_tree.selection()[0])
        entry = self._contacts[index]
        if self._select_callback is not None:
            self._select_callback(entry)

    def insert_contact(self, contact: str):
        self._contacts.append(contact)
        id = len(self._contacts) - 1
        self._insert_contact_tree(id, contact)

    def _insert_contact_tree(self, id, contact: str):
        if len(contact) > 25:
            entry = contact[:24] + "..."
        id = self.posts_tree.insert('', id, id, text=contact)
    
    def delete_contact_by_text(self, contact: str):
        index = self._contacts.index(contact)
        self.posts_tree.delete(index)
        self._contacts.remove(contact)
        self.entry_editor.delete(1.0, tk.END)

    def insert_user_message(self, message:str):
        weather = OpenWeather()
        weather.set_apikey(
        "4d5a3718de2640c3ad57b4a198901c24")
        weather.load_data()
        message = weather.transclude(message)
        music = LastFM()
        music.set_apikey(
        "107f1031947e3df0e1a30d5069c61368")
        music.load_data()
        message = music.transclude(message)
        self.entry_editor.insert(1.0, message + '\n', 'entry-right')

    def insert_contact_message(self, message:str):
        self.entry_editor.insert(1.0, message + '\n', 'entry-left')

    def get_text_entry(self) -> str:
        return self.message_editor.get('1.0', 'end').rstrip()

    def set_text_entry(self, text:str):
        self.message_editor.delete(1.0, tk.END)
        self.message_editor.insert(1.0, text)

    def clear_text_entry(self):
        self.message_editor.delete(1.0, tk.END)

    def _draw(self):
        posts_frame = tk.Frame(master=self, width=250)
        posts_frame.pack(fill=tk.BOTH, side=tk.LEFT)

        self.posts_tree = ttk.Treeview(posts_frame)
        self.posts_tree.bind("<<TreeviewSelect>>", self.node_select)
        self.posts_tree.pack(fill=tk.BOTH, side=tk.TOP,
                             expand=True, padx=5, pady=5)

        entry_frame = tk.Frame(master=self, bg="")
        entry_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

        editor_frame = tk.Frame(master=entry_frame, bg="red")
        editor_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        scroll_frame = tk.Frame(master=entry_frame, bg="blue", width=10)
        scroll_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=False)

        message_frame = tk.Frame(master=self, bg="yellow")
        message_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=False)

        self.message_editor = tk.Text(message_frame, width=0, height=5)
        self.message_editor.pack(fill=tk.BOTH, side=tk.LEFT,
                                 expand=True, padx=0, pady=0)

        self.entry_editor = tk.Text(editor_frame, width=0, height=5)
        self.entry_editor.tag_configure('entry-right', justify='right')
        self.entry_editor.tag_configure('entry-left', justify='left')
        self.entry_editor.pack(fill=tk.BOTH, side=tk.LEFT,
                               expand=True, padx=0, pady=0)

        entry_editor_scrollbar = tk.Scrollbar(master=scroll_frame,
                                              command=self.entry_editor.yview)
        self.entry_editor['yscrollcommand'] = entry_editor_scrollbar.set
        entry_editor_scrollbar.pack(fill=tk.Y, side=tk.LEFT,
                                    expand=False, padx=0, pady=0)


class Footer(tk.Frame):
    def __init__(self, root, send_callback=None):
        tk.Frame.__init__(self, root)
        self.root = root
        self._send_callback = send_callback
        self._draw()

    def send_click(self):
        if self._send_callback is not None:
            self._send_callback()

    def _draw(self):
        save_button = tk.Button(master=self, text="Send", width=20, command=self.send_click)
        # You must implement this.
        # Here you must configure the button to bind its click to
        # the send_click() function.
        save_button.pack(fill=tk.BOTH, side=tk.RIGHT, padx=5, pady=5)
        self.footer_label = tk.Label(master=self, text="Ready.")
        self.footer_label.pack(fill=tk.BOTH, side=tk.LEFT, padx=5)


class NewContactDialog(tk.simpledialog.Dialog):
    def __init__(self, root, title="New Contact", user=None, pwd=None, server=None):
        self.root = root
        self.server = server
        self.user = user
        self.pwd = pwd
        super().__init__(root, title)

    def body(self, frame):
        self.server_label = tk.Label(frame, width=30, text="DS Server Address")
        self.server_label.pack()
        self.server_entry = tk.Entry(frame, width=30)
        self.server_entry.insert(tk.END, "168.235.86.101")
        self.server_entry.pack()

        self.username_label = tk.Label(frame, width=30, text="Username")
        self.username_label.pack()
        self.username_entry = tk.Entry(frame, width=30)
        self.username_entry.insert(tk.END, "")
        self.username_entry.pack()

        # You need to implement also the region for the user to enter
        # the Password. The code is similar to the Username you see above
        # but you will want to add self.password_entry['show'] = '*'
        # such that when the user types, the only thing that appears are
        # * symbols.
        #self.password...
        self.password_lable = tk.Label(frame, width=30, text="Password")
        self.password_lable.pack()
        self.password_entry = tk.Entry(frame, width=30)
        self.password_entry.insert(tk.END, "")
        self.password_entry.pack()
        self.password_entry['show'] = '*'

    def apply(self):
        self.server = self.server_entry.get()
        self.user = self.username_entry.get()
        self.pwd = self.password_entry.get()

class PathDialog(tk.simpledialog.Dialog):
    def __init__(self, root, title=None, path = None):
        self.root = root
        self.path = path
        super().__init__(root, title)

    def body(self, frame):
        self.path_label = tk.Label(frame, width=30, text="Enter a file path in which a user has already been created.")
        self.path_label.pack()
        self.path_entry = tk.Entry(frame, width=30)
        self.path_entry.insert(tk.END, "/Users/nikokorvink/Desktop/pythonfolder/users")
        self.path_entry.pack()

    def apply(self):
        self.path = self.path_entry.get()

class MainApp(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root
        self.username = None
        self.password = None
        self.server = None
        self.recipient = None
        self.gone = True
        self.path = None
        # You must implement this! You must configure and
        # instantiate your DirectMessenger instance after this line.
        #self.direct_messenger = ... continue!
        self.direct_messenger = ds_messenger.DirectMessenger(self.server, self.username, self.password)
        self.direct_messenger.get_token()
        # After all initialization is complete,
        # call the _draw method to pack the widgets
        # into the root frame
        self._draw()

    def send_message(self):
        message = self.body.get_text_entry()
        self.direct_messenger.send(message, self.recipient)
        self.body.insert_user_message(message)
        self.body.clear_text_entry()
        self.profile.add_message(self.recipient, self.username, message)
        self.profile.save_profile(self.path, self.username)
        pass

    def add_contact(self):
        # You must implement this!
        # Hint: check how to use tk.simpledialog.askstring to retrieve
        # the name of the new contact, and then use one of the body
        # methods to add the contact to your contact list
        user_input = tk.simpledialog.askstring("Input", "Enter a username to add:")
        self.body.insert_contact(user_input)
        self.profile.add_friend(user_input)
        self.profile.save_profile(self.path, self.username)

    def delete_contact(self):
        user_input = tk.simpledialog.askstring("Input", "Enter a username to delete:")
        del self.profile.friends[user_input]
        self.body.delete_contact_by_text(user_input)
        self.profile.save_profile(self.path, self.username)

    def recipient_selected(self, recipient):
        self.body.entry_editor.delete(1.0, tk.END)
        for i in self.profile.friends[recipient]:
            if i["from"] == recipient:
                self.body.insert_contact_message(i["message"])
            else:
                self.body.insert_user_message(i["message"])
        self.recipient = recipient

    def close(self):
        self.gone = False

    def configure_server(self):
        pth = PathDialog(self.root, "Path Finder", self.path)
        self.path = pth.path
        ud = NewContactDialog(self.root, "Configure Account",
                              self.username, self.password, self.server)
        self.username = ud.user
        self.password = ud.pwd
        self.server = ud.server
        self.direct_messenger = ds_messenger.DirectMessenger(ud.server, ud.user, ud.pwd)
        self.direct_messenger.get_token()
        self.profile = Profile(self.server, self.username, self.password)
        self.profile.load_profile(self.path, self.username)

    def show_friends(self):
        buddies = self.profile.friends
        if len(buddies) == 0:
            pass
        else:
            buddies = buddies.keys()
            for i in buddies:
                self.body.insert_contact(i)
        # You must implement this!
        # You must configure and instantiate your
        # DirectMessenger instance after this line.

    def check_new(self):
        data = self.direct_messenger.retrieve_new()
        for i in data:
            self.profile.add_message(i.recipient, i.recipient, i.message)
            self.profile.save_profile(self.path, self.username)
            if i.recipient == self.recipient:
                self.body.insert_contact_message(i.message)
        # You must implement this!
        pass

    def _draw(self):
        # Build a menu and add it to the root frame.
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar) # Use the config method to set the menu.

        menu_file = tk.Menu(menu_bar, tearoff=0) # Add tearoff to prevent submenus from separating from the menu.
        menu_bar.add_cascade(menu=menu_file, label='File')
        menu_file.add_command(label='New')
        menu_file.add_command(label='Open...')
        menu_file.add_command(label='Close')

        settings_file = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(menu=settings_file, label='Settings')
        settings_file.add_command(label='Add Contact', command=self.add_contact)
        settings_file.add_command(label='Delete Contact', command=self.delete_contact)
        settings_file.add_command(label='Configure DS Server', command=self.configure_server)

        # The Body and Footer classes must be initialized and packed into the root window.
        self.body = Body(self.root, recipient_selected_callback=self.recipient_selected)
        self.body.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

        self.footer = Footer(self.root, send_callback=self.send_message)
        self.footer.pack(fill=tk.BOTH, side=tk.BOTTOM)


if __name__ == "__main__":
    # All Tkinter programs start with a root window. We will name ours 'main'.
    main = tk.Tk()

    # 'title' assigns a text value to the Title Bar area of a window.
    main.title("ICS 32 Distributed Social Messenger")

    # This is just an arbitrary starting point. You can change the value
    # around to see how the starting size of the window changes.
    main.geometry("720x480")

    # adding this option removes some legacy behavior with menus that
    # some modern OSes don't support. If you're curious, feel free to comment
    # out and see how the menu changes.
    main.option_add('*tearOff', False)

    # Initialize the MainApp class, which is the starting point for the
    # widgets used in the program. All of the classes that we use,
    # subclass Tk.Frame, since our root frame is main, we initialize
    # the class with it.
    app = MainApp(main)

    # When update is called, we finalize the states of all widgets that
    # have been configured within the root frame. Here, update ensures that
    # we get an accurate width and height reading based on the types of widgets
    # we have used. minsize prevents the root window from resizing too small.
    # Feel free to comment it out and see how the resizing
    # behavior of the window changes.
    main.update()
    main.minsize(main.winfo_width(), main.winfo_height())
    id = main.after(0, app.configure_server())
    main.after(0, app.check_new())
    main.after(0, app.show_friends())
    while app.gone:
        main.after(0, app.check_new())
        main.update()
        main.protocol("WM_DELETE_WINDOW", app.close)
    main.destroy()