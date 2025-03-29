class CircularQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None] * self.max_size
        self.front = 0
        self.rear = -1
        self.current_size = 0

    def is_empty(self):
        return self.current_size == 0

    def is_full(self):
        return self.current_size == self.max_size

    def size(self):
        return self.current_size

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
            return
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = item
        self.current_size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return -1
        removed_item = self.queue[self.front]
        self.front = (self.front + 1) % self.max_size
        self.current_size -= 1
        return removed_item


def add_task(task, task_list, queue):
    if len(task_list)<queue.max_size and task not in task_list:
        task_list.append(task)
        queue.enqueue(task)
    


def display_to_do_list(task_list):
    # write the code to print to do list
    for task in task_list:
        print(task)


def main():
    n = 10
    max_size = 101
    task_list = []
    task_queue = CircularQueue(max_size)

    # Read up to 10 tasks from input and add them to the to-do list
    for _ in range(n):
        task = int(input())
        add_task(task, task_list, task_queue)

    # Display the current to-do list
    display_to_do_list(task_list)


if __name__ == "__main__":
    main()
