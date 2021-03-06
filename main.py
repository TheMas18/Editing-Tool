import tkinter as tk
from tkinter import ttk
from editBar import EditBar
from imageViewer import ImageViewer



class Main(tk.Tk):

    def __init__(self, master=None, bg="black"):
        tk.Tk.__init__(self,master)
        self.master=master
        self.bg=bg

        self.filename = ""
        self.original_image = None
        self.processed_image = None
        self.Texted_image = None
        self.created_image = None
        self.is_image_selected = False
        self.mirror = False
        self.is_draw_state = False
        self.write_text = None
        self.is_crop_state = False

        self.filter_frame = None
        self.adjust_frame = None
        self.image_tools = None



        label=tk.Label(text="IMAGE  EDITOR",bg="#572347",height=1,width=100,fg="white")
        Font_tuple = ("Gabriola","30","bold")

        label.configure(font=Font_tuple)
        label.pack()



        self.editbar = EditBar(master=self)
        separator1 = ttk.Separator(master=self, orient=tk.HORIZONTAL)
        self.image_viewer = ImageViewer(master=self)

        self.editbar.pack(pady=20)
        separator1.pack(fill=tk.X, padx=20, pady=5)
        self.image_viewer.pack(fill=tk.BOTH, padx=20, pady=5, expand=1)





