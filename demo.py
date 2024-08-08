import os

font_path = "C:/Windows/Fonts/calibril.ttf"
if os.path.exists(font_path):
    print("Font file exists.")
else:
    print("Font file does not exist.")
