from tkinter import Frame, Button, LEFT
from PIL import Image, ImageDraw, ImageFont
from filterFrame import FilterFrame
from adjustFrame import AdjustFrame
from imageTools import ImageFrame
from PIL import Image
from tkinter import *
from tkinter.ttk import *
from matplotlib import pyplot as plt

import cv2
from tkinter import filedialog
import numpy as np
import tkinter.font as font



class EditBar(Frame):

    def __init__(self, master=None,bg="blue"):
        Frame.__init__(self, master)
        self.master = master
        self.master.configure(background="#daa4ca",bd=5)

        self.new_button = Button(self, text="New")
        self.camera_button = Button(master=self, text="Camera")
        self.save_button = Button(self, text="Save")
        self.save_as_button = Button(self, text="Save As")
        self.draw_button = Button(self, text="Draw")
        self.crop_button = Button(self, text="Crop")
        self.filter_button = Button(self, text="Filter")
        self.adjust_button = Button(self, text="Adjust")
        self.tools_button = Button(self, text="Tools")
        self.border_button = Button(self, text="Border")
        self.sketch_button = Button(self, text="Sketch")

        self.clear_button = Button(self, text="Clear")
        self.merge_button = Button(master=self, text="Merge")



        self.new_button.bind("<ButtonRelease>", self.new_button_released)
        self.camera_button.bind("<ButtonRelease>", self.camera_button_released)
        self.save_button.bind("<ButtonRelease>", self.save_button_released)
        self.save_as_button.bind("<ButtonRelease>", self.save_as_button_released)
        self.draw_button.bind("<ButtonRelease>", self.draw_button_released)
        self.crop_button.bind("<ButtonRelease>", self.crop_button_released)
        self.filter_button.bind("<ButtonRelease>", self.filter_button_released)
        self.adjust_button.bind("<ButtonRelease>", self.adjust_button_released)
        self.tools_button.bind("<ButtonRelease>", self.tools_button_released)
        self.clear_button.bind("<ButtonRelease>", self.clear_button_released)
        self.border_button.bind("<ButtonRelease>", self.border_button_released)
        self.sketch_button.bind("<ButtonRelease>", self.sketch_button_released)
        self.merge_button.bind("<ButtonRelease>", self.merge_button_released)

        self.new_button.pack(side=LEFT,ipadx=10,ipady=4)
        self.camera_button.pack(side=LEFT, ipadx=10, ipady=4)
        self.save_button.pack(side=LEFT,ipadx=10,ipady=4)
        self.save_as_button.pack(side=LEFT, ipadx=10,ipady=4)
        self.draw_button.pack(side=LEFT,ipadx=10,ipady=4)
        self.crop_button.pack(side=LEFT,ipadx=10,ipady=4)
        self.filter_button.pack(side=LEFT,ipadx=10,ipady=4)
        self.adjust_button.pack(side=LEFT,ipadx=10,ipady=4)
        self.tools_button.pack(side=LEFT, ipadx=10, ipady=4)
        self.border_button.pack(side=LEFT,ipadx=10,ipady=4)
        self.sketch_button.pack(side=LEFT, ipadx=10, ipady=4)
        self.clear_button.pack(side=LEFT,ipadx=10,ipady=4)
        self.merge_button.pack(padx=5, ipadx=10, ipady=4)




    def new_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.new_button:

            if self.master.is_draw_state:
                self.master.image_viewer.deactivate_draw()
            if self.master.is_crop_state:
                self.master.image_viewer.deactivate_crop()

            filename = filedialog.askopenfilename()
            image = cv2.imread(filename)



            if image is not None:
                self.master.filename = filename
                self.master.original_image = image.copy()
                self.master.processed_image = image.copy()
                self.master.image_viewer.show_image()
                self.master.is_image_selected = True

    def save_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.save_button:
            if self.master.is_image_selected:
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                save_image = self.master.processed_image
                image_filename = self.master.filename
                cv2.imwrite(image_filename, save_image)

    def save_as_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.save_as_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()

                original_file_type = self.master.filename.split('.')[-1]
                filename = filedialog.asksaveasfilename()
                filename = filename + "." + original_file_type

                save_image = self.master.processed_image
                cv2.imwrite(filename, save_image)

                self.master.filename = filename

    def camera_button_released(self, event):
        win_cam = cv2.VideoCapture(0)


        while True:
            retrieve, frame = win_cam.read()
            if not retrieve:
                print("failed to grab frame")
                break

            cv2.imshow("test", frame)

            k = cv2.waitKey(1)

            if k % 256 == 27:
                print("Escape hit, closing the app")
                break

            elif k % 256 == 32:
                img_name = "opencv_frame.png"
                cv2.imwrite(img_name, frame)
                print("screenshot taken")


        win_cam.release()
        img = cv2.imread('C:\\Users\\acer\\Downloads\\image editor (3)\\image editor\\opencv_frame.png')
        image = cv2.imwrite('E:\\Pranu\\opencv_processed.png', img)

        win_cam.destroyAllWindows()

    def draw_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.draw_button:
            if self.master.is_image_selected:
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                else:
                    self.master.image_viewer.activate_draw()




        myFont = font.Font(family='Helvetica', size=20, weight='bold')
        draw_button= Button(gui, text='Draw', bg='#0052cc', fg='#ffffff')

        draw_button['font'] = myFont
        self.draw_button.pack()
        root.mainloop()


    def sketch_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.sketch_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                   self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                   self.master.image_viewer.deactivate_crop()

                image = self.master.processed_image
                gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                inverted_gray_image = 255 - gray_img
                blurred_img = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)
                inverted_blurred_img = 255 - blurred_img
                pencil_sketch_IMG = cv2.divide(gray_img, inverted_blurred_img, scale=256.0)
                self.master.processed_image = pencil_sketch_IMG
                self.master.image_viewer.show_image(img=self.master.processed_image)



    def crop_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.crop_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                else:
                    self.master.image_viewer.activate_crop()

                root = mainloop()
                root.geometry('500x300')
                style = Style()

                root.mainloop()


    def border_button_released(self, event):

        if self.winfo_containing(event.x_root, event.y_root) == self.border_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()

                image = self.master.processed_image
                image = cv2.copyMakeBorder(image, 50, 50, 50, 50, cv2.BORDER_CONSTANT)
                self.master.processed_image = image
                self.master.image_viewer.show_image(img=self.master.processed_image)





    def adjust_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.adjust_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()

                self.master.adjust_frame = AdjustFrame(master=self.master)
                self.master.adjust_frame.grab_set()

    def filter_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.filter_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()

                self.master.filter_frame = FilterFrame(master=self.master)
                self.master.filter_frame.grab_set()


    def tools_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.tools_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()

                self.master.image_frame = ImageFrame(master=self.master)
                self.master.image_frame.grab_set()



    def clear_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.clear_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()

                self.master.processed_image = self.master.original_image.copy()
                self.master.image_viewer.show_image()
                style = ttk.Style()



    def merge_button_released(self, event):

        if self.winfo_containing(event.x_root, event.y_root) == self.merge_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                   self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                   self.master.image_viewer.deactivate_crop()

                filename1 = filedialog.askopenfilename()
                img1 = cv2.imread(filename1)

                filename2 = filedialog.askopenfilename()
                img2 = cv2.imread(filename2)
                im_h = cv2.hconcat([img1, img2])
                self.master.image_viewer.show_image(img=im_h)
                self.master.processed_image = im_h
                self.master.image_viewer.show_image(img=self.master.processed_image)

