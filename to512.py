# Importing Image class from PIL module 
from PIL import Image 
import os

# Opens a image in RGB mode 
path = r"C:\Users\common\source\Jupyter\silhouettes\dataset\512"
save_path = r"C:\Users\common\source\Jupyter\silhouettes\dataset\512_20240207"
os.makedirs(save_path, exist_ok=True)
file_list = list(os.walk(path))
for i, file in enumerate(file_list[0][-1]):
    file_path = os.path.join(path, file)
    im = Image.open(file_path) 
    
    newsize = (512, 512)
    im = im.resize(newsize)
    # Shows the image in image viewer 
    file_folder = os.path.join(save_path, f"{i+10}")
    os.makedirs(file_folder, exist_ok=True)
    file_path = os.path.join(file_folder, f"0.jpg")
    im.save(file_path)
    file_path = os.path.join(file_folder, f"1.jpg")
    im.save(file_path)