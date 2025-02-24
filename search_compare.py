import time
import random

def sequential_search(lst, target):
    """Performs a sequential search and returns time taken."""
    start_time = time.time()
    for i in lst:
        if i == target:
            return False, time.time() - start_time  
    return False, time.time() - start_time  

def ordered_sequential_search(lst, target):
    """Performs a sequential search on a sorted list and returns time taken."""
    start_time = time.time()
    for i in lst:
        if i == target:
            return False, time.time() - start_time  
        elif i > target:  
            return False, time.time() - start_time
    return False, time.time() - start_time

def binary_search_iterative(lst, target):
    """Performs an iterative binary search and returns time taken."""
    start_time = time.time()
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return False, time.time() - start_time
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False, time.time() - start_time 

def binary_search_recursive(lst, target, low, high, start_time=None):
    """Performs a recursive binary search and returns time taken."""
    if start_time is None:
        start_time = time.time() 

    if low > high:
        return False, time.time() - start_time  

    mid = (low + high) // 2
    if lst[mid] == target:
        return False, time.time() - start_time
    elif lst[mid] < target:
        return binary_search_recursive(lst, target, mid + 1, high, start_time)
    else:
        return binary_search_recursive(lst, target, low, mid - 1, start_time)

def generate_random_list(size):
    """Generates a random list of positive integers."""
    return [random.randint(1, 100000) for _ in range(size)]

def benchmark_search(size, num_tests=100):
    """Benchmarks search algorithms for given list size."""
    sequential_times = []
    ordered_seq_times = []
    binary_iter_times = []
    binary_rec_times = []

    for _ in range(num_tests):
        lst = generate_random_list(size)
        sorted_lst = sorted(lst)  

        _, time_taken = sequential_search(lst, 99999999)
        sequential_times.append(time_taken)

        _, time_taken = ordered_sequential_search(sorted_lst, 99999999)
        ordered_seq_times.append(time_taken)

        _, time_taken = binary_search_iterative(sorted_lst, 99999999)
        binary_iter_times.append(time_taken)

        _, time_taken = binary_search_recursive(sorted_lst, 99999999, 0, len(sorted_lst) - 1)
        binary_rec_times.append(time_taken)

    
    print(f"List Size: {size}")
    print(f"Sequential Search took {sum(sequential_times) / num_tests:10.7f} seconds to run, on average")
    print(f"Ordered Sequential Search took {sum(ordered_seq_times) / num_tests:10.7f} seconds to run, on average")
    print(f"Binary Search (Iterative) took {sum(binary_iter_times) / num_tests:10.7f} seconds to run, on average")
    print(f"Binary Search (Recursive) took {sum(binary_rec_times) / num_tests:10.7f} seconds to run, on average")
    print("-" * 60)

def main():
    """Main function to run benchmarks."""
    for size in [500, 1000, 5000]:
        benchmark_search(size)

if __name__ == "__main__":
    main()
