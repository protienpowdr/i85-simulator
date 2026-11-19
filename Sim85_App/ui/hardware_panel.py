import customtkinter as ctk
from CTkTable import *
from ui.sim85_vtables import AppTableView

class AppHardwarePanel(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master,fg_color="#1D1E1E",corner_radius=5)
        self.grid_rowconfigure(0,weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)
        self.grid_rowconfigure(4, weight=0)
        self.grid_rowconfigure(5, weight=0)
        self.grid_rowconfigure(6, weight=0)
        self.grid_rowconfigure(7, weight=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=0)

        self.label1 = ctk.CTkLabel(self,text="REGISTER ARRAY",font=("Oswald",16),justify="left")
        self.label2 = ctk.CTkLabel(self, text="MEMORY", font=("Oswald", 16), justify="left")
        self.label3 = ctk.CTkLabel(self, text="IO PORTS", font=("Oswald", 16), justify="left")

        reg_table = [["A/F","00","00"],["B/C", "00", "00"],["D/E", "00", "00"], ["H/L", "00", "00"],["PC", "00", "00"],["SP", "00", "00"]]
        flag_table = [["S","Z","K","AC","-","P","V","CY"], ['0','0','0','0','0','0','0','0']]


        self.register_array = CTkTable(self,row=6,column=3,values=reg_table,hover_color="#2a2d2e",corner_radius=0,font=("JetBrains Mono",12))
        self.flag_array = CTkTable(self,row=2,column=8,values=flag_table,hover_color="#2a2d2e",corner_radius=0,font=("JetBrains Mono",12))
        for i in range(0, 8):
            self.flag_array.frame[0,i].configure(width=10)
            self.flag_array.frame[1, i].configure(width=10)

        self.memory_address_selector = ctk.CTkEntry(self,placeholder_text="Enter address range :",font=("JetBrains Mono",12),width=250,text_color="#fb660a",fg_color="#1f1f1f",corner_radius=2)
        self.memory_panel = AppTableView(self,font=("JetBrains Mono",10),corner_radius=0,border_width=0,row_count=0,headers=["ADDRESS","DATA"])
        self.ports_panel = AppTableView(self,font=("JetBrains Mono",10),corner_radius=0,border_width=0,row_count=0,headers=["PORT","ADDRESS"])
        self.view_range_button = ctk.CTkButton(self,fg_color="gray17",hover_color="#242424",text="View",font=("JetBrains Mono",12), compound="left",width=80,corner_radius=2)
        self.clear_range_button = ctk.CTkButton(self, fg_color="gray17", hover_color="#242424", text="Clear",font=("JetBrains Mono", 12), compound="left", width=80,corner_radius=2)

        self.label1.grid(row=0,column=0,sticky="w",padx=20,pady=(10,0),columnspan=3)
        self.register_array.grid(row=1,column=0,sticky="nsew",padx=20,pady=(5,20),columnspan=3)
        self.flag_array.grid(row=2,column=0,sticky="nsew",padx=20,pady=(5,20),columnspan=3)
        self.label2.grid(row=3,column=0,sticky="w",padx=20,pady=(0,5),columnspan=3)
        self.label3.grid(row=6, column=0, sticky="w", padx=20, pady=(0,5),columnspan=3)

        self.memory_address_selector.grid(row=4, column=0, sticky="nsew", padx=(20,5), pady=(0, 10))
        self.view_range_button.grid(row=4,column=1,sticky="e",padx=5,pady=(0,10))
        self.clear_range_button.grid(row=4, column=2, sticky="e", padx=(5,20),pady=(0,10))
        self.memory_panel.grid(row=5,column=0,padx=20,pady=(0,20),sticky="nsew",columnspan=3)
        self.ports_panel.grid(row=7,column=0,padx=20,pady=(0,20),sticky="nsew",columnspan=3)



