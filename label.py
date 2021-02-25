

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk



class MyWindow(Gtk.Window):
lyrics = """Hi!"""
    def __init__(self):
        super(MyWindow, self).__init__()

        self.init_ui()

    def init_ui(self):    
        
        self.set_border_width(15)
        
        label = Gtk.Label(lyrics)
        self.add(label)

        self.set_title("Hi")
        self.set_size_request(250, 180)
        

        

win = MyWindow()
win.show_all()
Gtk.main()
