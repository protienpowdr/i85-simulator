from pathlib import Path

class SourceFileObject:
    __slots__ = ('filename','filedata','file_extension','filepath')
    def __init__(self,path):
        self.filepath = Path(path)
        self.filedata = self.filepath.read_text()
        self.file_extension = self.filepath.suffix
        self.filename = self.filepath.name


class FileHandler:
    def __init__(self):
        self.assembler_path = "bin/"
        self.assembler_binary = "asm85.exe"
        self.newfile_name = "untitled_program.asm"
        self.current_file_path = None
        self.is_file_opened = True

    def open_source_file(self,path):
        self.current_file_path = path
        self.is_file_opened = True
        return SourceFileObject(path)


    def save_file(self,data)-> bool:

        if not self.is_file_opened:
            return False
        else:
            with open(self.current_file_path,"w") as file:
                file.write(data)
            return True

    def save_as(self,data,path):
        with open(path,"w") as file:
            file.write(data)
            self.is_file_opened = True
            self.current_file_path = path
        return True

    def get_current_filename(self):
        if self.is_file_opened:
            return Path(self.current_file_path).name
        else:
            return self.newfile_name







class AppHandler:
    def __init__(self):
        self.file_handler = FileHandler()










