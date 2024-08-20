import threading
import time

# Global variable shared among threads
shared_variable = 0

# Create a lock
lock = threading.Lock()

# Function to increment the shared variable
def increment():
    global shared_variable
    for _ in range(10):
        # Acquire the lock before modifying the shared variable
        lock.acquire()
        shared_variable += 1
        # Release the lock after modifying the shared variable
        lock.release()

# Create multiple threads to increment the shared variable
threads = []
for _ in range(5):
    thread = threading.Thread(target=increment)
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Print the final value of the shared variable
print("Final value of shared variable:", shared_variable)