def find_common_elements(array1, array2):
    # Convert both arrays to sets and find their intersection
    common_elements = list(set(array1) & set(array2))
    
    # Print the common elements
    print("Common elements:", common_elements)
    
    return common_elements

# Example usage
array1 = input("Enter the elements of the first array, separated by spaces: ").split()
array2 = input("Enter the elements of the second array, separated by spaces: ").split()

# Call the function and store common elements in a new array
common_array = find_common_elements(array1, array2)
