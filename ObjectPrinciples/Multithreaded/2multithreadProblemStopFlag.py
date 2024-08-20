import threading
import time

# Global list to store integers
integer_list = []

# Flag to indicate whether the thread should stop
stop_flag = False

# Thread function for inserting elements into the list
def insert_thread():
    global stop_flag
    try:
        while len(integer_list) < 5 and not stop_flag:
            # Insert an element into the list
            integer_list.append(len(integer_list) + 1)
            print("Inserted:", len(integer_list))
            # Simulate some work between insertions
            time.sleep(0.005)  # 5 ms
    except KeyboardInterrupt:
        print("InsertThread interrupted.")
    finally:
        print("InsertThread stopped.")


# Create and start the InsertThread
insert_thread_instance = threading.Thread(target=insert_thread)
insert_thread_instance.start()

try:
    # Monitor the size of the list
    while len(integer_list) < 5:
        time.sleep(1)  # Check every second
    # Set the stop flag to True to interrupt the InsertThread
    stop_flag = True
    # Wait for the InsertThread to complete its execution
    insert_thread_instance.join()
    
except KeyboardInterrupt:
    print("Main thread interrupted.")

