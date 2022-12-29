class Dog:
    def __init__(self, group, country, color):
        self.name = "Dog"
        self.group = group
        self.country = country
        self.color = color
        
    def __rept__(self):
        return f'Dog (name = {self.name}, group = {self.group},'\
f' country = {self.country}, color = {self.color})'
    
