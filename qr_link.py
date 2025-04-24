import qrcode
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import webbrowser

def generate_qr():
    url = entry_url.get()
    if not url:
        messagebox.showwarning("Warning", "Please enter a URL.")
        return

    # Ask user where to save the QR code
    filepath = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png")],
                                             title="Save QR Code",
                                             initialfile="qr_code.png")
    if not filepath:
        return

    # Generate and save the QR code
    qr = qrcode.make(url)
    qr.save(filepath)

    # Open the folder where the file is saved
    folder_path = os.path.dirname(filepath)
    webbrowser.open(folder_path)

    messagebox.showinfo("Success", f"QR code saved to:\n{filepath}")

# GUI setup
app = tk.Tk()
app.title("QR Code Generator")

label_url = tk.Label(app, text="Enter URL:")
label_url.pack(pady=5)

entry_url = tk.Entry(app, width=50)
entry_url.pack(pady=5)

button_generate = tk.Button(app, text="Generate QR Code", command=generate_qr)
button_generate.pack(pady=10)

app.mainloop()
