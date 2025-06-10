class LearningError(Exception):
    ...

try:
    raise LearningError("Criando meu próprio erro")
except LearningError as error:
    error.add_note("Esse erro ocorreu para fins educativos")
    raise 