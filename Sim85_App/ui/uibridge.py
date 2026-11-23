from ui.app_handler import AppHandler
from ui.appinterface import AppWidgetType as Awt

class UiBridge:
    def __init__(self,mainwindow):
        self.window = mainwindow
        self.handler =AppHandler()

    def request_file_open(self):
        print("File Open Requested")
        print("File Dialog will open here")
        file = self.handler.file_handler.open_source_file("test.asm")
        print("File Opened")

        # Wd is the text editor, Sequence follows, Clear Old Code, Insert New Code
        editor = self.window.get_widget(Awt.SourceEditor)
        toolbar = self.window.get_widget(Awt.ToolBar)
        editor.clear_code()
        editor.insert_code(file.filedata)
        toolbar.update_filename_display(file.filename)


