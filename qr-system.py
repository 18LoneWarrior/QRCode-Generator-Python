import qrcode
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

'''
qrcode: Library to generate QR codes.
PIL (Pillow): Used for image processing and display.
tkinter: Standard Python interface to the Tk GUI toolkit.
ttk: Provides themed widgets.
filedialog and messagebox: Used for file dialogs and message boxes.
'''

'''The application is built using Python and leverages the tkinter library for the graphical user interface (GUI). 
The code is organized into sections that handle imports, function definitions, GUI configuration, and the main event 
loop. The application allows users to input text, generate a QR code from the text, display the QR code, and save the 
QR code as an image file.'''


# Defining function for generating qr code image
def createQR(*args):
    data = text_entry.get()
    if data:
        img = qrcode.make(data)
        resized_img = img.resize((280, 250))
        img_new = ImageTk.PhotoImage(resized_img)
        qr_canvas.delete("all")
        qr_canvas.create_image(100, 15, anchor=tk.NW, image=img_new)
        qr_canvas.image = img_new
    else:
        messagebox.showerror("Error", "Input text is required to generate QR code.")


# Defining function for saving the qr image to the system
def saveQR(*args):
    data = text_entry.get()
    if data:
        img = qrcode.make(data)
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            img.save(save_path)
            messagebox.showinfo("Success", f"QR code saved to {save_path}")
    else:
        messagebox.showerror("Error", "Input text is required to save QR code.")


# GUI Configurations
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("500x500")
root.config(bg="#403d39")
root.resizable(0, 0)

# frame1 is for the cover page
frame1 = tk.Frame(root, bd=2, relief=tk.RAISED)
frame1.place(x=10, y=5, width=480, height=280)
# frame2 is for button section
frame2 = tk.Frame(root, bd=2, relief=tk.SUNKEN)
frame2.place(x=10, y=300, width=480, height=190)
# Defining the cover image.
cover_img_path = "cover.jpg"
try:
    # Selecting the cover image and then covert it to ImageTk format.
    cover_img = Image.open(cover_img_path)
    cover_img = cover_img.resize((480, 250))
    cover_img = ImageTk.PhotoImage(cover_img)
# Error handling in case cover image doens't exist or failed to load.
except Exception as e:
    cover_img = None
    messagebox.showerror("Error", f"Failed to load cover image: {e}")

# Display the canvas image in frame1
qr_canvas = tk.Canvas(frame1)
if cover_img:
    qr_canvas.create_image(0, 15, anchor=tk.NW, image=cover_img)
    qr_canvas.image = cover_img
qr_canvas.pack(fill=tk.BOTH)

# Defining the text box in frame2
text_entry = ttk.Entry(frame2, width=45, font=("Sitka small", 11), justify="center")
text_entry.place(x=8, y=60)
# Defining the buttons in frame2.
btn_1 = ttk.Button(frame2, text="Generate", width=20, command=createQR)
btn_1.place(x=30, y=130)
btn_2 = ttk.Button(frame2, text="Save", width=20, command=saveQR)
btn_2.place(x=180, y=130)
btn_3 = ttk.Button(frame2, text="Exit", width=20, command=root.quit)
btn_3.place(x=320, y=130)

root.mainloop()
