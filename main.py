import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class PhotoGallery:
    def __init__(self, root):
        self.root = root
        self.root.title("Photo Gallery")
        self.root.geometry("800x600")

        self.images = []
        self.current_image_index = 0

        self.display_area = tk.Label(self.root)
        self.display_area.pack(expand=True)

        self.controls_frame = tk.Frame(self.root)
        self.controls_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.prev_button = tk.Button(self.controls_frame, text="Previous", command=self.prev_image)
        self.prev_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.next_button = tk.Button(self.controls_frame, text="Next", command=self.next_image)
        self.next_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.load_button = tk.Button(self.controls_frame, text="Load Images", command=self.load_images)
        self.load_button.pack(side=tk.RIGHT, padx=10, pady=10)

    def load_images(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        if file_paths:
            self.images = file_paths
            self.current_image_index = 0
            self.show_image()

    def show_image(self):
        if self.images:
            image_path = self.images[self.current_image_index]
            image = Image.open(image_path)
            image.thumbnail((800, 600))
            photo = ImageTk.PhotoImage(image)
            self.display_area.config(image=photo)
            self.display_area.image = photo

    def next_image(self):
        if self.images:
            self.current_image_index = (self.current_image_index + 1) % len(self.images)
            self.show_image()

    def prev_image(self):
        if self.images:
            self.current_image_index = (self.current_image_index - 1) % len(self.images)
            self.show_image()

if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoGallery(root)
    root.mainloop()
