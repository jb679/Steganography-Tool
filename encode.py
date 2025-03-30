from PIL import Image
import numpy as np

def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def encode_image(image_path, secret_text, output_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = np.array(img)
    
    binary_text = text_to_binary(secret_text) + '1111111111111110'  # End marker
    binary_index = 0
    
    for row in pixels:
        for pixel in row:
            for i in range(3):  # RGB channels
                if binary_index < len(binary_text):
                    pixel[i] = (pixel[i] & ~1) | int(binary_text[binary_index])
                    binary_index += 1
                else:
                    break
    
    encoded_img = Image.fromarray(pixels)
    encoded_img.save(output_path)
    print(f"Message encoded and saved as {output_path}")

if __name__ == "__main__":
    input_image = "input.png"  # Example input file
    output_image = "encoded.png"  # Example output file
    secret_message = "Hello, World!"
    
    encode_image(input_image, secret_message, output_image)
