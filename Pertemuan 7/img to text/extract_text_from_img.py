import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract

class ImageToTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image-to-Text Converter")

        self.image_path = None
        self.text_output = tk.StringVar()

        self.create_ui()
        
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    def create_ui(self):
        # Choose image file button
        self.choose_file_button = tk.Button(self.root, text="Choose Image File", command=self.choose_image)
        self.choose_file_button.pack(pady=10)

        # Display image
        self.image_label = tk.Label(self.root)
        self.image_label.pack()

        # Convert button
        self.convert_button = tk.Button(self.root, text="Convert to Text", command=self.convert_image_to_text, state="disabled")
        self.convert_button.pack(pady=10)

        # Text output
        self.text_output_label = tk.Label(self.root, textvariable=self.text_output)
        self.text_output_label.pack()

    def choose_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
        if self.image_path:
            self.convert_button["state"] = "normal"
            self.display_image()

    def display_image(self):
        image = Image.open(self.image_path)
        image = image.resize((300, 300), resample=Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BICUBIC)
        photo = ImageTk.PhotoImage(image)

        self.image_label.config(image=photo)
        self.image_label.image = photo

    def convert_image_to_text(self):
        # path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        
        # pytesseract.tesseract_cmd = path_to_tesseract

        if self.image_path:
            image = Image.open(self.image_path)
            text = pytesseract.image_to_string(image)
            self.text_output.set(text)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageToTextApp(root)
    root.mainloop()
