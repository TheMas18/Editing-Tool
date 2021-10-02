from tkinter import Toplevel, Button, RIGHT,Label
import tkinter as tk
from tkinter import filedialog
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
import cv2



class ImageFrame(Toplevel):

    def __init__(self, master=None):
        Toplevel.__init__(self, master=master,bg="#b4f5ce",highlightcolor="green")

        self.Tools_label = Label(self, text=" EDITING TOOLS",fg="black",bg="light green",height=2,width=12)

        self.Tools_label.pack()

        self.original_image = self.master.processed_image
        self.processing_image = None

        self.mirror_button = Button(master=self, text="Mirror",fg="black")
        self.flip_button = Button(master=self, text="Flip",fg="black")
        self.rotate_button = Button(master=self, text="Rotate",fg="black")
        self.cancel_button = Button(master=self, text="Cancel",fg="black")

        self.mirror_button.bind("<ButtonRelease>", self.mirror_button_released)
        self.flip_button.bind("<ButtonRelease>", self.flip_button_released)
        self.rotate_button.bind("<ButtonRelease>", self.rotate_button_released)
        self.cancel_button.bind("<ButtonRelease>", self.cancel_button_released)


        self.flip_button.pack(padx=5,ipadx=5,ipady=3,pady=3)
        self.rotate_button.pack(padx=5,ipadx=5,ipady=3,pady=3)
        self.mirror_button.pack(padx=5, ipadx=5, ipady=3, pady=3)
        self.cancel_button.pack(side=RIGHT,padx=5,ipadx=5,ipady=3)


    def mirror_button_released(self, event):
        self.mirror_button_released()
        self.show_image()

    def flip_button_released(self, event):
        self.flip_button_released()
        self.show_image()

    def rotate_button_released(self, event):
        self.rotate_button_released()
        self.show_image()

    def cancel_button_released(self, event):
        self.master.image_viewer.show_image()
        self.close()

    def show_image(self):
        self.master.image_viewer.show_image(img=self.processing_image)
        self.show_image()



    def mirror_button_released(self, event, with_plot=False):

        if self.winfo_containing(event.x_root, event.y_root) == self.mirror_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()

                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()

                image = self.master.processed_image
                image_mirror = np.fliplr(image)
                if with_plot:
                    fig = plt.figure(figsize=(10, 20))
                    ax1 = fig.add_subplot(2, 2, 1)
                    ax1.axis("off")
                    ax1.title.set_text('Original')
                    ax2 = fig.add_subplot(2, 2, 2)
                    ax2.axis("off")
                    ax2.title.set_text("Mirrored")
                    ax1.self.master.image_viewer.show_image(img=image)
                    ax2.self.master.image_viewer.show_image(img=image_mirror)
                    return True
                self.master.processed_image = image_mirror
                self.master.image_viewer.show_image(img=self.master.processed_image )


    def flip_button_released(self, event):

        if self.winfo_containing(event.x_root, event.y_root) == self.flip_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()

                img = self.master.processed_image
                self.master.image_viewer.show_image(img=img)

                img_flip = cv2.flip(img, 0)
                self.master.processed_image = img_flip
                self.master.image_viewer.show_image(img=self.master.processed_image)


    def rotate_button_released(self, event):

        if self.winfo_containing(event.x_root, event.y_root) == self.rotate_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()

                img = self.master.processed_image
                img_rotate_90_clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
                self.master.image_viewer.show_image(img=img_rotate_90_clockwise)
                self.master.processed_image = img_rotate_90_clockwise
                self.master.image_viewer.show_image(img=self.master.processed_image)


                img_rotate_90_counterclockwise = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
                self.master.image_viewer.show_image(img=img_rotate_90_counterclockwise)
                self.master.processed_image = img_rotate_90_clockwise
                self.master.image_viewer.show_image(img=self.master.processed_image)


                img_rotate_180 = cv2.rotate(img, cv2.ROTATE_180)
                self.master.image_viewer.show_image(img=img_rotate_180)
                self.master.processed_image = img_rotate_90_clockwise
                self.master.image_viewer.show_image(img=self.master.processed_image)















