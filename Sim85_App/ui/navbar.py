import customtkinter as ctk

class AppNavbar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master,corner_radius=0)

        self.grid_columnconfigure(0, weight=1)
        #self.grid_columnconfigure(1, weight=1)

        self.status = ctk.CTkCheckBox(self,corner_radius=50,checkbox_height=14,checkbox_width=14,
                                      text="Simulation stopped.",checkmark_color="green",
                                      hover_color="gray17",
                                      fg_color="green",border_color="red",
                                      font=("JetBrains Mono",12),
                                      state=ctk.DISABLED,
                                      text_color="gray")

        self.status.grid(column=0,row=0,sticky="w",padx=10)


        self.version = ctk.CTkLabel(self,text="v0.010 - Developed by Baibhav Bhattacharya",font=("JetBrains Mono",10))
        self.version.grid(column=1,row=0,sticky="E",padx=10)

    def update_status(self,status):
        if status:
            self.status.select()
            self.status.configure(text="Running...",text_color="white")
        else:
            self.status.deselect()
            self.status.configure(text="Simulation stopped.",text_color="gray")

