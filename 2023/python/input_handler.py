class InputHandler:

    def __init__(self, data: list = None) -> None:
        if data is None:
            self.data = list()
        else:
            self.data = data

    @classmethod
    def with_file_input(cls, filename: str = None):
        if filename is None:
            return cls()
        with open(filename, 'r') as file:
            file_content = file.readlines()
        return cls(file_content)
