import random


array = [random.randint(1, 100) for i in range(1, 100)] 
print(f"Array: {array}")

# Linear search function
def linear_search(array, num_to_find):  # O(n)
    for index, num in enumerate(array, start=0):
        if num == num_to_find:
            return index
    return -1

# Binary search function
def binary_search(array, lb, ub, num_to_find):  # O(log n)
    sorted_array = sorted(array)  
    if lb <= ub:
        mid = (ub + lb) // 2
        
        if sorted_array[mid] == num_to_find:
            return mid
        
        elif num_to_find < sorted_array[mid]:
            return binary_search(sorted_array, lb, mid-1, num_to_find)
        else:
            return binary_search(sorted_array, mid + 1, ub, num_to_find)
    else:
        return -1


num_to_find = int(input("Enter a number to find: "))
search_to_use = input("Which search would you like to use (linear/binary): ").lower()


if search_to_use == "linear":
    result_position = linear_search(array, num_to_find)
    if result_position != -1:
        print(f"Linear search: {num_to_find} was found at position {result_position + 1}")
    else:
        print(f"Linear search: {num_to_find} was not found in the array")


elif search_to_use == "binary":
    sorted_array = sorted(array)  
    result_position = binary_search(sorted_array, 0, len(sorted_array) - 1, num_to_find)
    if result_position != -1:
        print(f"Binary search: {num_to_find} was found at position {result_position + 1} in the sorted array {sorted_array}")
    else:
        print(f"Binary search: {num_to_find} was not found in the array")
else:
    print("Invalid search method")
