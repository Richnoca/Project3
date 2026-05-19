# Min-Heap with Task Scheduler Example

class Task:
    def __init__(self, name, priority, deadline):
        self.name = name
        self.priority = priority
        self.deadline = deadline

    def __lt__(self, other): # Define less than for comparison in the heap
        if self.priority == other.priority:
            return self.deadline < other.deadline
        return self.priority < other.priority #lower priority number means higher priority / comes first

    def __repr__(self): # how task prints.
        return f"{self.name} | Priority: {self.priority} | Deadline: {self.deadline}"

class MinHeap:
    def __init__(self):
        self.heap = [] # stores heap as array

    def is_empty(self): # true if heap is empty
        return len(self.heap) == 0

    def parent(self, index): # index of a nodes parent
        return (index - 1) // 2

    def left_child(self, index): # index of nodes left child
        return 2 * index + 1

    def right_child(self, index): # index of nodes right child
        return 2 * index + 2

    def insert(self, item): # Insert an item into the heap: O(log n)
        self.heap.append(item)
        self.bubble_up(len(self.heap) - 1)

    def bubble_up(self, index): # Move an item up until the heap property is restored
        while index > 0:
            parent_index = self.parent(index)

            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def peek(self): # Return the root without removing it: O(1)
        if self.is_empty():
            return "Heap is empty"
        return self.heap[0]

    def extract_min(self): # Remove and return the smallest item: O(log n)
        if self.is_empty():
            return "Heap is empty"

        if len(self.heap) == 1: # If there is only one item, just remove it
            return self.heap.pop()

        smallest = self.heap[0] # Save the root

        self.heap[0] = self.heap.pop() # Move last item to root and bubble it down
        self.bubble_down(0)

        return smallest

    def bubble_down(self, index):  #Move an item down until the heap property is restored
        while True:
            left = self.left_child(index)
            right = self.right_child(index)
            smallest = index

            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left # Check if left child is smaller

            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right # Check if right child is smaller

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest # Swap if a child is smaller than the current item
            else:
                break

    def heapify(self, array):
        self.heap = array[:]  # Build a heap from an unsorted array: O(n)

        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.bubble_down(i) # Start at the last parent node and bubble down each parent

    def heap_sort(self, array):
        self.heapify(array) # Heap sort using the min-heap

        sorted_array = []
        while not self.is_empty():
            sorted_array.append(self.extract_min())

        return sorted_array

    def verify_heap_property(self): # Check that every parent is smaller than its children
        for i in range(len(self.heap)):
            left = self.left_child(i)
            right = self.right_child(i)

            if left < len(self.heap) and self.heap[left] < self.heap[i]:
                return False
            
            if right < len(self.heap) and self.heap[right] < self.heap[i]:
                return False

        return True


def test_basic_heap(): # tester cases min heap here
    print("--- MIN-HEAP TEST ---")
    heap = MinHeap()
    numbers = [45, 12, 33, 5, 89, 23, 1, 67, 34, 90,
               2, 17, 8, 50, 29, 10, 77, 3, 15, 60]

    print("\nInserting 20 numbers:")
    for number in numbers:
        heap.insert(number)

    print(heap.heap)
    print("\nPeek at minimum:")
    print(heap.peek())
    print("\nExtracting 5 numbers:")

    for i in range(5):
        print(heap.extract_min())

    print("\nHeap after extractions:")
    print(heap.heap)
    print("\nHeap property still valid?")
    print(heap.verify_heap_property())


def test_heapify(): #heapify test cases here
    print("\n--- HEAPIFY TEST ---")
    numbers = [20, 5, 15, 22, 9, 13, 27, 1, 3, 30]
    heap = MinHeap()

    print("\nOriginal array:")
    print(numbers)
    heap.heapify(numbers)
    print("\nAfter heapify:")
    print(heap.heap)
    print("\nHeap property valid?")
    print(heap.verify_heap_property())

def test_heap_sort(): # sorter test cases here
    print("\n--- HEAP SORT TEST ---")
    numbers = [40, 10, 30, 50, 20, 5, 60, 15]
    heap = MinHeap()

    print("\nOriginal array:")
    print(numbers)

    sorted_numbers = heap.heap_sort(numbers)
    print("\nSorted array:")
    print(sorted_numbers)

def test_task_scheduler(): # task scheduler test cases here
    print("\n--- TASK SCHEDULER ---")
    task_heap = MinHeap()
    tasks = [
        Task("Study", 1, "2026-05-19"),
        Task("Finish alg2 video", 1, "2026-05-20"),
        Task("Submit Theory of comp", 2, "2026-05-20"),
        Task("Review heap youtube video", 2, "2026-05-19"),
        Task("Prepare 399 video", 2, "2026-05-18"),
        Task("Reply to work emails", 3, "2026-05-19"),
        Task("Feed dogs", 3, "2026-05-23"),
        Task("Do laundry", 4, "2026-05-22"),
        Task("Clean desk", 5, "2026-05-25"),
        Task("Organize garage", 4, "2026-05-21")
    ]

    print("\nAdding tasks:")
    for task in tasks:
        task_heap.insert(task)
        print("Added:", task)
    print("\nNext task to complete:")
    print(task_heap.peek())
    print("\nCompleting tasks in order:")
    while not task_heap.is_empty():
        print(task_heap.extract_min())

def test_edge_cases(): # edge case test cases here
    print("\n--- Test edge cases ---")
    heap = MinHeap()
    print("\nExtract from empty heap:")
    print(heap.extract_min())
    print("\nPeek empty heap:")
    print(heap.peek())
    print("\nInsert one number:")
    heap.insert(100)
    print(heap.heap)
    print("\nExtract one number:")
    print(heap.extract_min())
    print("\nHeap after removing only item:")
    print(heap.heap)

def main():
    test_basic_heap()
    test_heapify()
    test_heap_sort()
    test_task_scheduler()
    test_edge_cases()

main()
