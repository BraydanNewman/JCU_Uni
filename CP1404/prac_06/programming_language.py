class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing.lower() == 'dynamic'

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
