from CTkCodeBox import *
from ui.i85lexer import I85Lexer
import customtkinter as ctk

class AppMainEditor(CTkCodeBox):
    def __init__(self, master):
        super().__init__(master=master,
        language=I85Lexer,
        font=ctk.CTkFont("JetBrains Mono",16),
        theme="fruity",
        menu=False,
        undo=True,)

        self._textbox.configure(font=ctk.CTkFont("JetBrains Mono", 16))
        self._start = "1.0"
        self._end = "end"

    def get_code(self):
        return self.get("1.1","end")

    def insert_code(self,text):
        super().insert(self._start, text, None)




class AssemblerOutput(ctk.CTkTextbox):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)

        # Configure text tags for colors
        self.tag_config("success", foreground="white")
        self.tag_config("error", foreground="red")

        # Disable by default
        self.configure(state="disabled")

    def print_success(self, message):
        self.configure(state="normal")
        self.insert("end", message + "\n", "success")
        self.configure(state="disabled")
        self.see("end")

    def print_error(self, message):
        self.configure(state="normal")
        self.insert("end", message + "\n", "error")
        self.configure(state="disabled")
        self.see("end")




class ListingView(ctk.CTkTextbox):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)

        # Add Listing
        self.tag_config("listing", foreground="white")
        self.insert(0.0,"Program Listing view.", "listing")
        self.configure(state="disabled")


    def clear_listing(self):
        self.delete(0.0,"end")

    def add_listing(self,listing):
        self.clear_listing()
        self.configure(state="normal")
        self.insert("end", listing, "listing")