from Dog import Dog
class Beagle(Dog):
    def __init__(self, group, country, age, max_height):
        super().__init__(group, country, color)
        self.name = "Beagle"
        self.age = age
        self.max_height = max_height
    def __repr__(self):
        return f'Dog (name = {self.name}, group = {self.group},' \
f' country = {self.country} \ color = {self.color}, age = {self.age},'\
f' max_weight = {self.max_weight})'
