class fake_tuple:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __getitem__(self, item):
        if item == 0:
            return self.a
        elif item == 1:
            return self.b
        else:
            raise IndexError("Index out of range")