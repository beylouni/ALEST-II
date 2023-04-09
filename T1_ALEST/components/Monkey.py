class Monkey():
    def __init__(self, id, even, odd, coconuts):
        self.id = id
        self.even_destination = even
        self.odd_destionation = odd
        self.coconuts = coconuts

    def get_id(self):
        return self.id
    def get_even_destination(self):
        return self.even_destination
    def get_odd_destination(self):
        return self.odd_destionation
    def get_coconuts(self):
        return self.coconuts
    
    def add_coconut(self, v):
        self.coconuts += [v]
    def reset_coconuts(self):
        self.coconuts = []