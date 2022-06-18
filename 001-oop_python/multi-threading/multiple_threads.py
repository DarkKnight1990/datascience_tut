import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    threads = list()
    for index in range(3):
        logging.info("Main  : create and start thread %d", index + 1)
        x = threading.Thread(target=thread_function, args=(index + 1, ))
        threads.append(x)
        x.start()
    
    for index, thread in enumerate(threads):
        logging.info("Main  : before joining thread %d", index + 1)
        thread.join()
        logging.info("Main  : thread %d is done", index + 1)
    logging.info("Main  : all done!")
