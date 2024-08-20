import threading
import time

# Create an event object
stop_event = threading.Event()

def my_thread_function():
    while not stop_event.is_set():
        print("Thread is running...")
        time.sleep(0.01)  # Simulate some work

# Create and start the thread
my_thread = threading.Thread(target=my_thread_function)
my_thread.start()

# Wait for 50 milliseconds
time.sleep(0.05)

# Set the event to interrupt the thread
print("Interrupting the thread...")
stop_event.set()

# Wait for the thread to finish
my_thread.join()

print("Main thread: Done!")