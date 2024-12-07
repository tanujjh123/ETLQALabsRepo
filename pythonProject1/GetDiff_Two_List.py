def get_list_differences(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    difference = list(set1.symmetric_difference(set2))
    return difference

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

differences = get_list_differences(list1, list2)
print("Differences:")
print(differences)
