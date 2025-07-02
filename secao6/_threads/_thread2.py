from threading import Thread
from time import sleep

class Doingthings(Thread):
    def __init__(self, text: str, time: int) -> None:
        self.text = text
        self.time = time

        # Ao criar uma classe que herda de Threads é necessário que
        # ao final de seu construtor adicione um super().__init__()
        super().__init__() 

    def run(self):
        sleep(self.time)
        print(self.text)

thread01 = Doingthings('thread001', 5)
thread01.start()

thread02 = Doingthings('thread002', 12)
thread02.start()

for i in range(10):
    sleep(1)
    print(i)