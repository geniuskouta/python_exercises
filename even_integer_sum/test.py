def get_sum_positive_even(numbers):
    sum = 0
    for num in numbers:
        if num % 2 == 0 and num > 0:
            sum += num
    print(sum)

get_sum_positive_even([1, 2, 3, 4, 5, -1, 9])
get_sum_positive_even([1, 3, 5, 7])
get_sum_positive_even([])
