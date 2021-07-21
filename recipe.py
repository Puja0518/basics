class Recipe:
    def __init__(self, name , ingrident, chef):
        self.names = name
        self.ingrident = ingrident
        self.chf = chef

ingdrident = ["rice","masala","chicken"]
book = Recipe("biryani",ingdrident, "Puja")
print(book.chef)