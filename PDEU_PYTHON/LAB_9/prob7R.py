def average_list(lst, count=0, total=0):
    if not lst:
        return total / count if count != 0 else 0
    return average_list(lst[1:], count + 1, total + lst[0])

lst = list(map(int, input("Enter numbers separated by space: ").split()))
print("Average:", average_list(lst))

# Input: [4, 8, 12]
# Output: 8.0
