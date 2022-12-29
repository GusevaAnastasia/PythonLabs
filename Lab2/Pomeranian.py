from Dog import Dog
class Pomeranian(Dog):
    def __init__(self, group, color, age):
        super().__init__(group, country, color)
        self.name = "Pomeranian"
        self.age = age
    def __repr__(self):
        return f'Dog (name = {self.name}, group = {self.group},'\
f' country = {self.country} \ color = {self.color}, age = {self.age})'
        
