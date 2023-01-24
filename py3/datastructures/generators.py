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


# GENERATOR WITH yield keyword


def square_number(nums):
    for i in nums:
        yield i * i


result_1 = list(square_number(list_))
# if we print next(square_number(list_))
# we print the first element in the generator
# you need to convert it to list
print(result_1)
print(next(square_number(list_)))

# print the generator with for loop


for num in square_number(list_):
    print(num)

nums = [x * x for x in square_number(list_)]
print(nums)

# generator comprehension
nums = (x * x for x in square_number(list_))
print(nums)

