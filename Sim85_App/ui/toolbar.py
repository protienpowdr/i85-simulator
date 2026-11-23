import customtkinter as ctk
from ui.appassets import AppAsset
from ui.appinterface import AppFunction as Af

class AppToolbar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master,corner_radius=0,height=40)
        self.grid_columnconfigure(0, weight = 0)
        self.grid_columnconfigure(1, weight = 0)
        self.grid_columnconfigure(2, weight = 0)
        self.grid_columnconfigure(3, weight = 0)
        self.grid_columnconfigure(4, weight = 0)
        self.grid_columnconfigure(5, weight = 1)
        self.grid_columnconfigure(6, weight = 0)
        self.grid_columnconfigure(7, weight=0)
        self.grid_columnconfigure(8, weight=0)
        self.grid_columnconfigure(9, weight=0)

        self.app_icon = ctk.CTkLabel(self,text="i85",font=("ADLaM Display",14),text_color="blue")

        self.new_btn = ctk.CTkButton(self,fg_color="transparent",text="New",text_color="white",font=("JetBrains Mono",12),width=20,hover_color="gray17")
        self.open_btn = ctk.CTkButton(self,fg_color="transparent",text="Open",text_color="white",font=("JetBrains Mono",12),width=20,hover_color="gray17")
        self.save_btn = ctk.CTkButton(self,fg_color="transparent",text="Save",text_color="white",font=("JetBrains Mono",12),width=20,hover_color="gray17")
        self.save_as_btn = ctk.CTkButton(self,fg_color="transparent",text="Save As",text_color="white",font=("JetBrains Mono",12),width=20,hover_color="gray17")
        self.start_button = ctk.CTkButton(self,fg_color="#487C4C",hover_color="#3D6940",text="Start",font=("JetBrains Mono",12), compound="left",width=60)
        self.step_button = ctk.CTkButton(self,fg_color="#1f1f1f",hover_color="#242424",text="Step",font=("JetBrains Mono",12), compound="left",width=60)
        self.reset_button = ctk.CTkButton(self,fg_color="#1f1f1f",hover_color="#242424",text="Reset",font=("JetBrains Mono",12), compound="left",width=80)
        self.start_address = ctk.CTkEntry(self,placeholder_text="Enter starting address Eg: 0000",font=("JetBrains Mono",12),width=245,text_color="#fb660a",fg_color="#1f1f1f")
        self.filename_display = ctk.CTkLabel(self,image=ctk.CTkImage(AppAsset.file_appicon),compound="left",text="untitled_program.asm",font=("JetBrains Mono",12))

        self._place_widgets()
        self._initialize_commands()


    def _initialize_commands(self):
        open_command = self.winfo_toplevel().get_function(Af.RequestFileOpen)
        self.open_btn.configure(command=open_command)


    def _place_widgets(self):
        self.app_icon.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.new_btn.grid(row=0, column=1, sticky="nsew", padx=5)
        self.open_btn.grid(row=0, column=2, sticky="nsew", padx=5)
        self.save_btn.grid(row=0, column=3, sticky="nsew", padx=5)
        self.save_as_btn.grid(row=0, column=4, sticky="nsew", padx=5)
        self.filename_display.grid(row=0, column=5, sticky="nsew", padx=20)
        self.start_address.grid(row=0, column=6, sticky="e", padx=5)
        self.step_button.grid(row=0, column=7, sticky="e", padx=5)
        self.start_button.grid(row=0, column=8, sticky="e", padx=5)
        self.reset_button.grid(row=0, column=9, sticky="w", padx=(5, 35))

    def update_filename_display(self,filename=None):
        if filename is None:
            self.filename_display.configure(text="Untitled_program.asm")
        else:
            self.filename_display.configure(text=filename)
