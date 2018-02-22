class Text:
    def __init__(self, message):
        self.message = message

    def upper(self):
        return str.upper(self.message)


class Number:
    def __init__(self, number):
        self.number = number

    def is_even(self):
        return self.number % 2 == 0

    def increase_by_one(self):
        self.number += 1


def main():  # pragma: no cover
    t = Text('Very interesting MeSsAgE')
    print(f'{t.message} vs {t.upper()}')

    n = Number(222)
    print(n.is_even)

    n = Number(333)
    print(n.is_even())


if __name__ == '__main__':
    main()
