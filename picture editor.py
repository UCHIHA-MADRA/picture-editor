
from PIL import Image
import os

def resize_and_compress_image(input_path, output_path, target_width_cm, target_height_cm, target_dpi, min_size_kb, max_size_kb):
    # Convert cm to pixels
    width_px = int(target_width_cm * target_dpi / 2.54)
    height_px = int(target_height_cm * target_dpi / 2.54)
    
    # Open the image
    try:
        img = Image.open(input_path)
    except FileNotFoundError:
        print(f"File not found: {input_path}")
        return
    
    # Resize the image
    img = img.resize((width_px, height_px), Image.Resampling.LANCZOS)
    
    # Save the image with varying quality to match file size requirements
    quality = 95  # Start with high quality
    while quality > 10:
        img.save(output_path, 'JPEG', quality=quality)
        file_size_kb = os.path.getsize(output_path) / 1024  # Get file size in KB
        print(f"Current file size: {file_size_kb:.2f} KB at quality: {quality}")
        if min_size_kb <= file_size_kb <= max_size_kb:
            print(f"Final file size: {file_size_kb:.2f} KB at quality: {quality}")
            break
        quality -= 5
    else:
        print("Could not compress image to the desired size range.")

# Input and output paths
input_path = 'C:\\Users\\Prabhu\\Downloads\\sign prabhu.jpg'  # Ensure this file exists in the directory or provide the correct path
output_path = 'C:\\Users\\Prabhu\\Downloads\\output.jpg'

# Target dimensions and file size requirements
target_width_cm = 6.0
target_height_cm = 2.0
target_dpi = 300
min_size_kb = 10
max_size_kb = 20

# Resize and compress the image
resize_and_compress_image(input_path, output_path, target_width_cm, target_height_cm, target_dpi, min_size_kb, max_size_kb)
