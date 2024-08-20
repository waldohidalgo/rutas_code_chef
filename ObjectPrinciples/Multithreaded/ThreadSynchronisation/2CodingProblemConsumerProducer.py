from threading import Semaphore, Thread

class SharedResource:
    def __init__(self):
        self.isProduced = False
        self.mutex = Semaphore(1)
        self.producerSemaphore = Semaphore(1)
        self.consumerSemaphore = Semaphore(0)

    def produce(self):
        self.producerSemaphore.acquire()
        self.mutex.acquire()
        
        if self.isProduced:
            self.mutex.release()
            self.consumerSemaphore.release()
            self.producerSemaphore.acquire()
            
        print("Producer produced")
        self.isProduced = True
        self.mutex.release()
        self.consumerSemaphore.release()

    def consume(self):
        self.consumerSemaphore.acquire()
        self.mutex.acquire()
        
        if not self.isProduced:
            self.mutex.release()
            self.producerSemaphore.release()
            self.consumerSemaphore.acquire()
            
        print("Consumer consumed")
        self.isProduced = False
        self.mutex.release()
        self.producerSemaphore.release()


sharedResource = SharedResource()

producerThread = Thread(target=sharedResource.produce)
consumerThread = Thread(target=sharedResource.consume)

producerThread.start()
consumerThread.start()

