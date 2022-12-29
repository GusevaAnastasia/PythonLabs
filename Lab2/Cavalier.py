from Dog import Dog
class Cavalier(Dog):
    def __init__(self, group, country, color, price):
        super().__init__(group, country, color)
        self.name = "Cavalier"
        self.price = price
    def __repr__(self):
        return f'Dog(name = {self.name}, group = {self.group}, country = {self.country},'\
               f'color = {self.color}, price = {self.price})'
