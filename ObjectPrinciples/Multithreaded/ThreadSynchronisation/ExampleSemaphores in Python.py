import threading
import time

# Define a semaphore with a maximum of 2 resources
semaphore = threading.Semaphore(2)

# Function to access the shared resource
def access_resource(thread_id):
    print(f"Thread {thread_id} is trying to acquire the semaphore.")
    # Acquire the semaphore
    semaphore.acquire()
    print(f"Thread {thread_id} has acquired the semaphore.")
    try:
        # Simulate accessing the shared resource
        print(f"Thread {thread_id} is accessing the shared resource.")
        time.sleep(0.002)
    finally:
        # Release the semaphore
        semaphore.release()
        print(f"Thread {thread_id} has released the semaphore.")

# Create multiple threads to access the shared resource
threads = []
for i in range(5):
    thread = threading.Thread(target=access_resource, args=(i,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All threads have completed their execution.")