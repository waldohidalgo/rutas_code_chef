import threading
import time

def my_thread_function():
    print("Thread started.")
    time.sleep(0.005)  # Simulate some work
    print("Thread finished.")

# Create and start the thread
my_thread = threading.Thread(target=my_thread_function)
my_thread.start()

# Interrupt the thread after 3 milliseconds
my_thread.join(timeout=0.003)
print("Main thread continued.")

# Wait for the thread to finish
my_thread.join()
print("Main thread: Done!")