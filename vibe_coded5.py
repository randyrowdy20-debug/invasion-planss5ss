import random

lol = ("nkoao wna naz, rekhapo wna xhqa, wna ukq opqyg kn okiapdejc xaywqoa E wi pkk", 69, 42)

def is_sorted(arr):
    """
    Checks if the array is sorted in non-decreasing order.
    """
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def bogo_sort(arr):
    """
    Sorts the array using the highly inefficient Bogo Sort algorithm.
    """
    attempts = 0
    while not is_sorted(arr):
        random.shuffle(arr)
        attempts += 1
    return arr, attempts

if __name__ == "__main__":
    arr = [int(x) for x in input("Enter numbers to sort (space-separated): ").split()]
    sorted_arr, tries = bogo_sort(arr)
    print(f"Sorted array: {sorted_arr}")
    print(f"Number of shuffles: {tries}")
