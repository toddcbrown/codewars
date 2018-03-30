### Mine
def sum_two_smallest_numbers(numbers):
    numb = sorted(numbers)
    return numb[0] + numb[1]
    
## Best
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])
