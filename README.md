# Cache Management Algorithms Homework

This repository contains solutions for homework tasks on cache management algorithms.

## Tasks
- **Task 1**: Optimize array query processing using LRU Cache.
- **Task 2**: Compare Fibonacci calculation performance using LRU Cache and Splay Tree.

## Files
- `lru_cache_array.py`: Solution for Task 1.
- `fibonacci_comparison.py`: Solution for Task 2.
- `requirements.txt`: Dependency list for the project.

## Requirements
- Python 3.x
- Libraries:
  - `numpy<2.0`
  - `matplotlib>=3.5.0`
  - `tabulate>=0.9.0`
- Install dependencies:
  ```bash
  pip3 install -r requirements.txt
  ```

## Usage
Run each script to test:
```bash
python3 lru_cache_array.py
python3 fibonacci_comparison.py
```

## Notes
- Task 1 generates a random array and queries; ensure sufficient memory for 100,000 elements.
- Task 2 outputs a table and graph comparing LRU Cache and Splay Tree performance.
- All scripts are tested on Python 3.11.