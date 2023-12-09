class InputHandler:
    def __init__(self, data: list = None) -> None:
        if data is None:
            self.data = list()
        else:
            self.data = data

    @staticmethod
    def with_file_input(filename: str = None) -> list[str]:
        if filename is None:
            return list()
        with open(filename, "r") as file:
            file_content: list[str] = file.readlines()
        return file_content

    @staticmethod
    def build_filepath_for_day(day_num: int) -> str:
        day_num = f"0{day_num}" if day_num < 10 else day_num
        return f"../resources/input-{day_num}.txt"
