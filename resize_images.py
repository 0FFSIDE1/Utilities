from PIL import Image
import os

# folder containing images
input_folder = input("Enter input folder path:\n")
output_folder = input("Enter output folder path:\n")
new_size = (385, 330)
format_mapping = {
    ".jpg": "JPEG",
    ".jpeg": "JPEG",
    ".png": "PNG",
    ".bmp": "BMP",
    ".gif": "GIF",
    ".webp": "WEBP"
}
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    file_ext = os.path.splitext(filename)[1].lower()  # Extract file extension
    if file_ext in format_mapping:
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        #resize
        img.thumbnail(new_size)  # Ensures it fits within dimensions without cropping
        # Save with the correct format
        save_path = os.path.join(output_folder, filename)
        img.save(save_path, format=format_mapping[file_ext])
    
print("Resizing completed!")

