class sequence_repeat:
    def __init__(self, sequence: str, repeat: int):
        self.sequence = sequence
        self.repeat = repeat
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.repeat - 1:
            raise StopIteration

        self.index += 1
        return self.sequence[self.index % len(self.sequence)]
