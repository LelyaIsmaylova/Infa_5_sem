import time
from threading import Thread

def calculate_partial_sum(array, start, end, result):
    partial_sum = sum(array[start:end]) 
    result.append(partial_sum) 

def parallel_sum(array, num_threads):
    result = []
    array_length = len(array)
    chunk_size = array_length // num_threads
    threads = []
  
    for i in range(num_threads):
        start = i * chunk_size
        end = start + chunk_size if i < num_threads-1 else array_length
        thread = Thread(target=calculate_partial_sum, args=(array, start, end, result))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    return sum(result)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num_threads in [1, 2, 4, 8]:
    start_time = time.time()
    total_sum = parallel_sum(numbers, num_threads) 
    elapsed_time = time.time() - start_time
    print(f"Number of threads: {num_threads}, Total sum: {total_sum}, Time elapsed: {elapsed_time} seconds")
