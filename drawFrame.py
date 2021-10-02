from tkinter import Toplevel, Button, RIGHT
import numpy as np
import cv2

class DrawFrame(Toplevel):

    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        self.original_image = self.master.processed_image
        self.Draw_image = None

        self.red_button = Button(master=self, text="Red")
        self.white_button = Button(master=self, text="White")
        self.blue_button = Button(master=self, text="Blue")
        self.black_button = Button(master=self, text="Black")
        self.green_button = Button(master=self, text="Green")
        self.yellow_button = Button(master=self, text="Yellow")
        self.cancel_button = Button(master=self, text="Cancel")
        self.apply_button = Button(master=self, text="Apply")

        self.red_button.bind("<ButtonRelease>", self.red_button_released)
        self.white_button.bind("<ButtonRelease>", self.white_released)
        self.blue_button.bind("<ButtonRelease>", self.blue_button_released)
        self.black_button.bind("<ButtonRelease>", self.black_button_released)
        self.green_button.bind("<ButtonRelease>", self.green_button_released)
        self.yellow_button.bind("<ButtonRelease>", self.yellow_button_released)
        self.apply_button.bind("<ButtonRelease>", self.apply_button_released)
        self.cancel_button.bind("<ButtonRelease>", self.cancel_button_released)

        self.red_button.pack(padx=21)
        self.white_button.pack()
        self.blue_button.pack()
        self.black_button.pack()
        self.green_blur_button.pack()
        self.yellow_blur_button.pack()
        self.cancel_button.pack(side=RIGHT)
        self.apply_button.pack()


    def close(self):
        self.destroy()
