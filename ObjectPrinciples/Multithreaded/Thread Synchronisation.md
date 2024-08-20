# Thread Synchronisation

Thread synchronization in Python involves coordinating the execution of multiple threads to ensure they access shared resources safely and avoid race conditions. Python provides several mechanisms for thread synchronization, including locks, semaphores, events, and conditions. These mechanisms help control access to shared resources and enable threads to communicate and coordinate with each other effectively.

Here's an overview of two common thread synchronization mechanisms in Python:

## Locks:

Locks are the most basic synchronization mechanism in Python. They allow only one thread to acquire the lock at a time.
The threading.Lock class provides a simple lock implementation that can be used to protect critical sections of code.
Threads acquire the lock using the acquire() method and release it using the release() method.

## Semaphores:

Semaphores are used to control access to a shared resource with limited capacity. They maintain a count representing the number of available resources.
The threading.Semaphore class provides semaphore objects that can be used to synchronize access to shared resources.
Threads acquire resources from the semaphore using the acquire() method and release them using the release() method.
