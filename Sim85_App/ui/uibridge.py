from ui.app_handler import AppHandler
from ui.appinterface import AppWidgetType as Awt
import tkinter.filedialog as fd

class UiBridge:
    def __init__(self,mainwindow):
        self.window = mainwindow
        self.handler =AppHandler()

    def request_file_open(self):
        path = fd.askopenfilename(title="Open File",filetypes=[("8085 Assembly Source","*.asm")],defaultextension=".asm")
        if not path:
            return
        file = self.handler.file_handler.open_source_file(path)

        # Wd is the text editor, Sequence follows, Clear Old Code, Insert New Code
        editor = self.window.get_widget(Awt.SourceEditor)
        toolbar = self.window.get_widget(Awt.ToolBar)
        editor.delete_code()
        editor.insert_code(file.filedata)
        toolbar.update_filename_display(file.filename)

    def request_new_file(self):
        editor = self.window.get_widget(Awt.SourceEditor)
        toolbar = self.window.get_widget(Awt.ToolBar)
        editor.delete_code()
        toolbar.update_filename_display(self.handler.file_handler.newfile_name)
        self.handler.file_handler.new_file_opened()

    def request_file_save(self):
        toolbar = self.window.get_widget(Awt.ToolBar)
        editor = self.window.get_widget(Awt.SourceEditor)
        data = editor.get_code()
        if not self.handler.file_handler.save_file(data):
            path = fd.asksaveasfilename(title="Save File",filetypes=[("8085 Assembly Source","*.asm")],defaultextension=".asm")
            if not path: return
            self.handler.file_handler.save_as(data,path)
            toolbar.update_filename_display(self.handler.file_handler.get_current_filename())

    def request_file_saveas(self):
        path = fd.asksaveasfilename(title="Save File As",filetypes=[("8085 Assembly Source","*.asm")],defaultextension=".asm")
        if not path:
            return

        toolbar = self.window.get_widget(Awt.ToolBar)
        editor = self.window.get_widget(Awt.SourceEditor)
        data = editor.get_code()
        self.handler.file_handler.save_as(data,path)
        toolbar.update_filename_display(self.handler.file_handler.get_current_filename())

