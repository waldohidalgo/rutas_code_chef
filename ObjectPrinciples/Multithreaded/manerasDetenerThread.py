#1 Using a shared variable or flag: You can use a shared variable or flag to signal the thread to stop its execution gracefully. The thread periodically checks the value of this flag and exits its loop or function if the flag is set.

import threading
import time

# Shared flag
stop_flag = False

def my_thread_function():
    while not stop_flag:
        # Thread's main task
        time.sleep(1)  # Simulate some work

# Create and start the thread
my_thread = threading.Thread(target=my_thread_function)
my_thread.start()

# Interrupt the thread
stop_flag = True


# 2 Using the Event object: The threading.Event class provides a more robust mechanism for interrupting threads. You can create an event object and set it to interrupt the thread's execution.

import threading
import time

# Create an event object
stop_event = threading.Event()

def my_thread_function():
    while not stop_event.is_set():
        # Thread's main task
        time.sleep(1)  # Simulate some work

# Create and start the thread
my_thread = threading.Thread(target=my_thread_function)
my_thread.start()

# Interrupt the thread
stop_event.set()

# 3.Using the Thread class's join() method: You can use the join() method to wait for the thread to complete its execution. By specifying a timeout, you can effectively interrupt the thread after a certain duration.

import threading
import time

def my_thread_function():
    while True:
        # Thread's main task
        time.sleep(1)  # Simulate some work

# Create and start the thread
my_thread = threading.Thread(target=my_thread_function)
my_thread.start()

# Interrupt the thread after 5 seconds
my_thread.join(timeout=5)