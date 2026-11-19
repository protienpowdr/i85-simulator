from ui.appassets import AppAsset
from ui.hardware_panel import AppHardwarePanel
from ui.navbar import AppNavbar
from ui.toolbar import AppToolbar
from ui.editor import AppMainEditor, AssemblerOutput, ListingView
from ui.app_handler import AppHandler
from ui.containers import WidgetContainer

import customtkinter as ctk

class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        # Font Configuration
        AppAsset.loadFonts()

        # Main Widget Container
        self.wdc = WidgetContainer(self)

        # Widget Groups
        self.LeftSidePanel = ctk.CTkFrame(self.wdc,width=30,corner_radius=0)
        self.RightSidePanel = ctk.CTkFrame(self.wdc,width=30,corner_radius=0)
        self.Navbar = AppNavbar(master=self.wdc)
        self.Toolbar = AppToolbar(master=self.wdc)
        self.Editor = AppMainEditor(master=self.wdc)
        self.HardwarePanel = AppHardwarePanel(master=self.wdc)
        self.AssemblerOut = AssemblerOutput(master=self.wdc,font=("JetBrains Mono",12))
        self.ProgramListingView = ListingView(master=self.wdc,font=("JetBrains Mono",12),width=360)

        # Resizing
        self._is_resizing = False
        self._resize_timer = None
        self._last_size = ()


        # Initialization
        self._initialize_window()
        self._configure_gridlayout()
        self._configure_widget_placement()
        self._set_window_styles()
        self._initialize_bindings()


    """
        basic customtkinter setup code, any styles and configurations using pywinstyles and ctk goes here
    """
    def _initialize_window(self):
        self.title("i85 Simulator & IDE")
        self.iconbitmap(AppAsset.main_appicon)
        self.geometry("1280x720")
        self.last_size = (self.winfo_width(), self.winfo_height())

    def _set_window_styles(self):
        ctk.set_appearance_mode("dark")


    """
        Configure the gridlayout of the wdc and the mainwindow, the wdc should occupy entirety of the mainwindow to act as 
        the main container
    """
    def _configure_gridlayout(self):

        # Main window Layout
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Widget Container Layout
        self.wdc.grid_rowconfigure(0, weight=0)
        self.wdc.grid_rowconfigure(1, weight=1)
        self.wdc.grid_rowconfigure(2, weight=0)
        self.wdc.grid_rowconfigure(3, weight=0)

        self.wdc.grid_columnconfigure(0, weight=0)
        self.wdc.grid_columnconfigure(1, weight=0)
        self.wdc.grid_columnconfigure(2, weight=1)
        self.wdc.grid_columnconfigure(3, weight=0)
        self.wdc.grid_columnconfigure(4, weight=0)


    """
        Set gridlayout of all the widgets inside wdc - WidgetContainer
    """
    def _configure_widget_placement(self):
        self.wdc.grid(row=0, column=0, sticky="nsew")
        self.Toolbar.grid(row=0, column=0, columnspan=5, sticky="nsew", pady=0)
        self.Navbar.grid(row=3, column=0, columnspan=5, sticky="nsew")
        self.HardwarePanel.grid(row=1, column=3, sticky="nsew", padx=(3, 5), pady=5, rowspan=2)
        self.Editor.grid(row=1, column=2, sticky="nsew", padx=5, pady=5)
        self.AssemblerOut.grid(row=2, column=2, sticky="nsew", padx=5, pady=4)
        self.ProgramListingView.grid(row=1, column=1, sticky="nsew", padx=(5, 3), pady=4, rowspan=2)
        self.LeftSidePanel.grid(row=1, column=0, sticky="ns", rowspan=2)
        self.RightSidePanel.grid(row=1, column=4, sticky="ns", rowspan=2)

    """
        Initialize bindings of all ui functions and widgets
    """
    def _initialize_bindings(self):
        self.bind("<Configure>", self._resize_window)


    """
        Hides the main widget container "mainwindow.wdc" while resizing to make the animation snappier and avoid dynamic calculation
        of many tabular widgets as it makes the resize animation significantly slower.
        The entire window appears in a minimum of 50ms from the resize release to avoid flickering-like effect
    """
    def _resize_window(self,event):
        if event.widget != self or (event.width,event.height) == self._last_size:
            return

        self._last_size = (event.width,event.height)
        if not self._is_resizing:
            self._is_resizing = True
            self.wdc.grid_forget()

        if self._resize_timer:
            self.after_cancel(self._resize_timer)


        # Resize end function
        def end_resizing():
            self._is_resizing = False
            self.wdc.grid(row=0,column=0,sticky="nsew")

        self._resize_timer = self.after(50, end_resizing)
