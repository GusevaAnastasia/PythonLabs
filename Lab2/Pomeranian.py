from Dog import Dog
class Pomeranian(Dog):
    def __init__(self, group, color, age, max_weight):
        super().__init__(group, country, color)
        self.name = "Pomeranian"
        self.age = age
        self.max_weight = max_weight
    def __repr__(self):
        return f'Dog (name = {self.name}, group = {self.group},'\
f' country = {self.country} \ color = {self.color}, age = {self.age},' \
f' max_weight = {self.max_weight})'
        
