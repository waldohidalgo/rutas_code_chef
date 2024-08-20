import threading

class Counter:
    def __init__(self):
        # Initialize the counter and a lock
        self.count = 0
        self.lock = threading.Lock()

    def increment(self):
        # Acquire the lock before modifying the counter
        with self.lock:
            self.count += 1

    def decrement(self):
        # Acquire the lock before modifying the counter
        with self.lock:
            self.count -= 1

    def get_count(self):
        # Acquire the lock before reading the counter
        with self.lock:
            return self.count


counter = Counter()

# Function to increment the counter
def increment_counter():
    for _ in range(1000):
        counter.increment()
        
# Function to decrement the counter
def decrement_counter():
    for _ in range(100):
        counter.decrement()
        
# Create two threads to increment and decrement the counter concurrently
thread1 = threading.Thread(target=increment_counter)
thread2 = threading.Thread(target=decrement_counter)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

# Print the final value of the counter
print("Final count:", counter.get_count())

