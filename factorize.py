import multiprocessing
import time

def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


def synchronous_factorize(numbers):
    return [factorize(number) for number in numbers]

numbers_list = [9913, 11777, 1234567, 987654321]
start_time = time.time()
result = synchronous_factorize(numbers_list)
end_time = time.time()
print("Синхронний час виконання:", end_time - start_time)
print("Результат:", result)

def parallel_factorize(numbers):
    with multiprocessing.Pool() as pool:
        return pool.map(factorize, numbers)

start_time = time.time()
result_parallel = parallel_factorize(numbers_list)
end_time = time.time()
print("Паралельний час виконання:", end_time - start_time)
print("Результат (паралельний):", result_parallel)
