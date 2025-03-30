import tkinter as tk
from tkinter import filedialog, messagebox
from encode import encode_image
from decode import decode_message

def encode():
    print("Encoding started")
    # Open file dialog to select the image
    image_path = filedialog.askopenfilename(title="Select an Image to Encode")
    if not image_path:
        return

    print(f"Selected image: {image_path}")

    # Ask for the secret message to encode
    message = message_entry.get()
    if not message:
        messagebox.showerror("Input Error", "Please enter a message to encode")
        return

    # Ask for output file path to save the image
    output_path = filedialog.asksaveasfilename(defaultextension=".png", title="Save Encoded Image")
    if not output_path:
        return

    print(f"Output path: {output_path}")

    # Encode the message into the image
    if encode_image(image_path, message, output_path):
        messagebox.showinfo("Success", "Message encoded successfully!")
        print(f"Encoded image saved at: {output_path}")
    else:
        messagebox.showerror("Encoding Failed", "Failed to encode the message")

def decode():
    print("Decoding started")
    # Open file dialog to select the image to decode
    image_path = filedialog.askopenfilename(title="Select an Image to Decode")
    if not image_path:
        return

    print(f"Selected image for decoding: {image_path}")

    # Decode the hidden message
    hidden_message = decode_message(image_path)
    if hidden_message:
        messagebox.showinfo("Decoded Message", f"Hidden Message: {hidden_message}")
    else:
        messagebox.showerror("Decoding Failed", "No hidden message found")

# Create the main window
print("Creating window")
window = tk.Tk()
window.title("Steganography Tool")

# Create a label and entry widget for the message input
message_label = tk.Label(window, text="Enter Message to Encode:")
message_label.pack(pady=5)
message_entry = tk.Entry(window, width=50)
message_entry.pack(pady=5)

# Create buttons for encoding and decoding
encode_button = tk.Button(window, text="Encode Message", command=encode)
encode_button.pack(pady=5)
decode_button = tk.Button(window, text="Decode Message", command=decode)
decode_button.pack(pady=5)

# Run the main loop
print("Starting main loop")
window.mainloop()
