import time
import random

def insertion_sort(lst):
    """Performs insertion sort and returns time taken."""
    start_time = time.time()
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return time.time() - start_time

def shell_sort(lst):
    """Performs shell sort and returns time taken."""
    start_time = time.time()
    gap = len(lst) // 2
    while gap > 0:
        for i in range(gap, len(lst)):
            temp = lst[i]
            j = i
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = temp
        gap //= 2
    return time.time() - start_time

def python_sort(lst):
    """Performs Python's built-in sort and returns time taken."""
    start_time = time.time()
    lst.sort()
    return time.time() - start_time

def generate_random_list(size):
    """Generates a random list of positive integers."""
    return [random.randint(1, 100000) for _ in range(size)]

def benchmark_sort(size, num_tests=100):
    """Benchmarks sorting algorithms for given list size."""
    insertion_times = []
    shell_times = []
    python_times = []

    for _ in range(num_tests):
        lst = generate_random_list(size)

        lst_copy = lst[:]
        insertion_times.append(insertion_sort(lst_copy))

        lst_copy = lst[:]
        shell_times.append(shell_sort(lst_copy))

        lst_copy = lst[:]
        python_times.append(python_sort(lst_copy))

    print(f"List Size: {size}")
    print(f"Insertion Sort took {sum(insertion_times) / num_tests:10.7f} seconds to run, on average")
    print(f"Shell Sort took {sum(shell_times) / num_tests:10.7f} seconds to run, on average")
    print(f"Python Sort took {sum(python_times) / num_tests:10.7f} seconds to run, on average")
    print("-" * 60)

def main():
    """Main function to run benchmarks."""
    for size in [500, 1000, 5000]:
        benchmark_sort(size)

if __name__ == "__main__":
    main()
