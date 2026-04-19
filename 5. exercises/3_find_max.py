def find_max(numbers:list[int]) -> int:
    if numbers == []:
        raise ValueError("The list cannot be empty.")
    largest = numbers[0]
    for number in numbers[1:]:  # 1: Start from the second element
        if number > largest:
            largest = number
    return largest

print(find_max([3, 5, 2, 8, 1])) 