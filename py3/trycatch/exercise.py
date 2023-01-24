def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i * i)

    return result


list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result_ = square_numbers(list_)

# or with comprehension
second_result = [x for x in square_numbers(list_)]

print(second_result)
