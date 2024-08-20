import threading
import time

# Shared flag
stop_flag = False

def my_thread_function():
    print("Thread started.")
    while not stop_flag:
        print("Thread is doing some work...")
        time.sleep(0.01)  # Simulate some work
    print("Thread stopped.")

# Create and start the thread
my_thread = threading.Thread(target=my_thread_function)
my_thread.start()

# Simulate some other work in the main thread
time.sleep(0.05)

# Interrupt the thread by setting the stop flag
print("Interrupting the thread.")
stop_flag = True

# Wait for the thread to complete
my_thread.join()
print("Main thread: Thread has completed.")