def sanitize_list(lst):
    if not lst:
        return []
    return [max(0, lst[0])] + sanitize_list(lst[1:])

lst = list(map(int, input("Enter numbers separated by space: ").split()))
print("Sanitized list:", sanitize_list(lst))

# Input: [-3, 5, -1, 7, 0, -10]
# Output: [0, 5, 0, 7, 0, 0]
