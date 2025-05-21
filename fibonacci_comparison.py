from functools import lru_cache
import timeit
import matplotlib.pyplot as plt
from tabulate import tabulate

class SplayNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class SplayTree:
    def __init__(self):
        self.root = None

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def _splay(self, key, root):
        if not root or root.key == key:
            return root

        if key < root.key:
            if not root.left:
                return root
            if key < root.left.key:
                root.left.left = self._splay(key, root.left.left)
                root = self._right_rotate(root)
            elif key > root.left.key:
                root.left.right = self._splay(key, root.left.right)
                if root.left.right:
                    root.left = self._left_rotate(root.left)
            return self._right_rotate(root) if root.left else root
        else:
            if not root.right:
                return root
            if key < root.right.key:
                root.right.left = self._splay(key, root.right.left)
                if root.right.left:
                    root.right = self._right_rotate(root.right)
            elif key > root.right.key:
                root.right.right = self._splay(key, root.right.right)
                root = self._left_rotate(root)
            return self._left_rotate(root) if root.right else root

    def insert(self, key, value):
        if not self.root:
            self.root = SplayNode(key, value)
            return
        self.root = self._splay(key, self.root)
        if self.root.key == key:
            self.root.value = value
            return
        new_node = SplayNode(key, value)
        if key < self.root.key:
            new_node.right = self.root
            new_node.left = self.root.left
            self.root.left = None
        else:
            new_node.left = self.root
            new_node.right = self.root.right
            self.root.right = None
        self.root = new_node

    def search(self, key):
        if not self.root:
            return None
        self.root = self._splay(key, self.root)
        return self.root.value if self.root.key == key else None

@lru_cache(maxsize=None)
def fibonacci_lru(n):
    if n <= 1:
        return n
    return fibonacci_lru(n-1) + fibonacci_lru(n-2)

def fibonacci_splay(n, tree):
    result = tree.search(n)
    if result is not None:
        return result
    if n <= 1:
        tree.insert(n, n)
        return n
    fn_1 = fibonacci_splay(n-1, tree)
    fn_2 = fibonacci_splay(n-2, tree)
    result = fn_1 + fn_2
    tree.insert(n, result)
    return result

def compare_fibonacci_methods():
    test_values = list(range(0, 951, 50))
    lru_times = []
    splay_times = []
    number_of_executions = 100

    for n in test_values:
        # Measure time for LRU cache
        lru_time = timeit.timeit(lambda: fibonacci_lru(n), number=number_of_executions) / number_of_executions
        lru_times.append(lru_time)

        # Measure time for Splay Tree
        tree = SplayTree()
        splay_time = timeit.timeit(lambda: fibonacci_splay(n, tree), number=number_of_executions) / number_of_executions
        splay_times.append(splay_time)

    # Create table
    table = [[n, f"{lru_time:.8f}", f"{splay_time:.8f}"] for n, lru_time, splay_time in zip(test_values, lru_times, splay_times)]
    print("\nn         LRU Cache Time (s)  Splay Tree Time (s)")
    print("--------------------------------------------------")
    print(tabulate(table, tablefmt="plain"))

    # Create chart
    plt.figure(figsize=(10, 6))
    plt.plot(test_values, lru_times, label="LRU Cache", color="blue")
    plt.plot(test_values, splay_times, label="Splay Tree", color="orange")
    plt.xlabel("n (Fibonacci number index)")
    plt.ylabel("Average Execution Time (seconds)")
    plt.title("Fibonacci Calculation: LRU Cache vs Splay Tree")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Analysis
    print("\nAnalysis:")
    print("LRU Cache generally outperforms Splay Tree for Fibonacci calculations, especially for larger values of n.")
    print("This is due to the simplicity and efficiency of the @lru_cache decorator, which provides O(1) access to cached values.")
    print("Splay Tree, while self-balancing, introduces overhead from rotations and node management, leading to slower performance.")

if __name__ == "__main__":
    compare_fibonacci_methods()