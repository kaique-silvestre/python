from dataclasses import dataclass, asdict, astuple

@dataclass
class Pessoa:
    nome: str = 'Eduardo'
    sobrenome: str = 'Junior'
    idade: int = '20'