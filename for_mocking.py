class Main:
    def __init__(self, status):
        self.status = status

    def format_status(self, times=1):
        return [f'Status: {self.status};'] * times

    def letter_generator(self):
        for letter in self.status:
            yield letter
