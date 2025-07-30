def reverse_list(lst):
    if len(lst) <= 1:
        return lst
    return [lst[-1]] + reverse_list(lst[:-1])

lst = list(map(int, input("Enter numbers separated by space: ").split()))
print("Reversed list:", reverse_list(lst))

# Input: [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]
