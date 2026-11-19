import customtkinter as ctk


class WidgetContainer(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master=master,
                         corner_radius=0,
                         fg_color="gray17")
