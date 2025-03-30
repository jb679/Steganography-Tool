from PIL import Image

def decode_message(image_path):
    img = Image.open(image_path)

    # Ensure the image is in RGB mode
    img = img.convert("RGB")
    
    pixels = img.load()
    
    binary_message = ""
    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]
            binary_message += str(r & 1)  # Extract LSB from red channel
            
            if len(binary_message) % 8 == 0 and binary_message[-8:] == "00000000":
                return binary_to_text(binary_message[:-8])
    
    return "No hidden message found"

def binary_to_text(binary_string):
    text = ""
    for i in range(0, len(binary_string), 8):
        text += chr(int(binary_string[i:i+8], 2))
    return text
