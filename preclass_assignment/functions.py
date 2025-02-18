import re

def greet(name):
    """Prints a greeting message."""
    print(f"Hello, {name}!")

def goldilocks(bed_size):
    """Prints if the bed is too small, too large, or just right."""
    if bed_size < 140:
        print("Too small!")
    elif bed_size > 150:
        print("Too large!")
    else:
        print("Just right. :)") if bed_size == 140 else print("Just right. :))")

def square_list(lst):
    """Returns a list of squared values."""
    return [x ** 2 for x in lst]

def fibonacci_stop(n):
    """Returns a list of Fibonacci numbers up to n."""
    fib_seq = [0, 1]
    while True:
        next_fib = fib_seq[-1] + fib_seq[-2]
        if next_fib > n:
            break
        fib_seq.append(next_fib)
    return fib_seq

def clean_pitch(pitch_angles, status_signals):
    """Cleans pitch angles by setting bad values to -999."""
    cleaned = []
    for angle, status in zip(pitch_angles, status_signals):
        if (angle < 0 or angle > 90) and status > 0:
            cleaned.append(-999)
        else:
            cleaned.append(angle)
    return cleaned