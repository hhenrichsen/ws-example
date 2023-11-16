from multiprocessing import Process, Queue
import uvicorn
from random import choice
from time import sleep
from app import app


def web(queue):
    app.queue = queue
    uvicorn.run(app)


def generator(queue):
    words = ["Hello", "World", "My", "Name", "Is", "John", "Doe"]

    while True:
        word = choice(words)
        print(f"[GEN]:\t Adding {word} to queue")
        queue.put(word)
        sleep(1)


if __name__ == "__main__":
    queue = Queue()
    generator_process = Process(target=generator, args=(queue,))
    web_process = Process(target=web, args=(queue,))
    generator_process.start()
    web_process.start()
