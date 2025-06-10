def create_repr(cls):
    def myrepr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        phrase = f"{class_name}({class_dict})"
        return phrase
    cls.__repr__ = myrepr
    return cls


@create_repr
class Pais:
    def __init__(self, nome):
        self.nome = nome



brasil = Pais('brasil')
print(brasil)