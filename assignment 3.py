
# Name: Igiebor Emmanuel Oluwafemi
# Matric Number: 230502027
# Course: Data Structures
# Assignment: Sorting Algorithm and Running Time


# Given array
array = [5, 8, 16, 10, 3, 14]

print("Original Array:", array)

# Bubble Sort Algorithm
n = len(array)

for i in range(n):
    for j in range(0, n - i - 1):
        if array[j] > array[j + 1]:
            # Swap elements
            array[j], array[j + 1] = array[j + 1], array[j]

print("Sorted Array:", array)

# Running Time Explanation
print("\nRunning Time Analysis (Bubble Sort):")
print("Best Case: O(n)")
print("Average Case: O(n^2)")
print("Worst Case: O(n^2)")
