from Dog import Dog
class Samoyed(Dog):
    def __init__(self, group, country, color, max_length):
        super().__init__(group, country, color)
        self.name = "Samoyed"
        self.max_length = max_length
    def __repr__(self):
        return f'Dog(name = {self.name}, group = {self.group}'\
               f' country = {self.country}, color = {self.color}'\
               f' max_length = {self.max_length})'
