class Main:
    def __init__(self, status):
        self.status = status

    def format_status(self):
        return f'Status: {self.status};'

    def letter_generator(self):
        for letter in self.status:
            yield letter
