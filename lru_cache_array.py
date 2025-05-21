import random
import time
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return None
        # Move to end to show it was recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def invalidate_range(self, index):
        # Invalidate cache entries affected by the updated index
        keys_to_remove = [key for key in self.cache if key[0] <= index <= key[1]]
        for key in keys_to_remove:
            self.cache.pop(key)

def range_sum_no_cache(array, L, R):
    return sum(array[L:R+1])

def update_no_cache(array, index, value):
    array[index] = value

def range_sum_with_cache(array, L, R, cache):
    key = (L, R)
    cached_result = cache.get(key)
    if cached_result is not None:
        return cached_result
    result = sum(array[L:R+1])
    cache.put(key, result)
    return result

def update_with_cache(array, index, value, cache):
    array[index] = value
    cache.invalidate_range(index)

def generate_test_data(array_size, num_queries):
    array = [random.randint(1, 1000) for _ in range(array_size)]
    queries = []
    for _ in range(num_queries):
        query_type = random.choice(['Range', 'Update'])
        if query_type == 'Range':
            L = random.randint(0, array_size-2)
            R = random.randint(L+1, array_size-1)
            queries.append(('Range', L, R))
        else:
            index = random.randint(0, array_size-1)
            value = random.randint(1, 1000)
            queries.append(('Update', index, value))
    return array, queries

def process_queries_no_cache(array, queries):
    start_time = time.time()
    for query in queries:
        if query[0] == 'Range':
            range_sum_no_cache(array, query[1], query[2])
        else:
            update_no_cache(array, query[1], query[2])
    return time.time() - start_time

def process_queries_with_cache(array, queries):
    cache = LRUCache(capacity=1000)
    start_time = time.time()
    for query in queries:
        if query[0] == 'Range':
            range_sum_with_cache(array, query[1], query[2], cache)
        else:
            update_with_cache(array, query[1], query[2], cache)
    return time.time() - start_time

if __name__ == "__main__":
    # Generate test data
    array_size = 100_000
    num_queries = 50_000
    array, queries = generate_test_data(array_size, num_queries)

    # Process queries without cache
    array_copy = array.copy()
    time_no_cache = process_queries_no_cache(array_copy, queries)

    # Process queries with cache
    array_copy = array.copy()
    time_with_cache = process_queries_with_cache(array_copy, queries)

    # Output results
    print(f"Час виконання без кешування: {time_no_cache:.2f} секунд")
    print(f"Час виконання з LRU-кешем: {time_with_cache:.2f} секунд")