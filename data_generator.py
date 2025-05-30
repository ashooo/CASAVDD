import random

def generate_data(size, distribution_type):
    if distribution_type == 'random':
        return [random.randint(0, size) for _ in range(size)]
    elif distribution_type == 'sorted':
        return list(range(size))
    elif distribution_type == 'reversed':
        return list(range(size, 0, -1))
    elif distribution_type == 'nearly_sorted':
        arr = list(range(size))
        for _ in range(size // 10):  
            i = random.randint(0, size - 1)
            j = random.randint(0, size - 1)
            arr[i], arr[j] = arr[j], arr[i]
        return arr
    else:
        raise ValueError(f"Unknown distribution type: {distribution_type}")
