class ResultHandler:
    def __init__(self, win, lose, draw):
        self.win = win.casefold()
        self.lose = lose.casefold()
        self.draw = draw.casefold()

    def get_result_from_string(self, text):
        if text.casefold() == self.win:
            return 1
        elif text.casefold() == self.lose:
            return 0
        elif text.casefold() == self.draw:
            return 0.5
        else:
            raise ValueError(
                f"Invalid result value[{text}], supported values are [{self.win}, {self.lose}, {self.draw}]"
            )
