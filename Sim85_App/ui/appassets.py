import customtkinter as _ctk
from PIL import Image as _Image

class AppAsset():
    path_font_monospace = "assets/fonts/jetbrains-mono.ttf"
    path_font_generic = "assets/fonts/trebuc.ttf"
    path_font_title = "assets/fonts/oswald.ttf"
    path_font_title2 = "assets/fonts/adlam-display.ttf"
    main_appicon = "assets/icons/app_main.ico"
    path_image_fileicon = "assets/icons/file.png"
    ASM85 = "bin/asm85.exe"
    file_appicon = _Image.open(path_image_fileicon)


    @classmethod
    def loadFonts(cls):
        _ctk.FontManager.load_font(cls.path_font_monospace)
        _ctk.FontManager.load_font(cls.path_font_generic)
        _ctk.FontManager.load_font(cls.path_font_title)
        _ctk.FontManager.load_font(cls.path_font_title2)




