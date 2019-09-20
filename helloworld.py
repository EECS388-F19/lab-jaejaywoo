import random

random_numbers = [random.randint(0, 100) for _ in range(2)]
_sum = sum(random_numbers)
_avg = _sum / len(random_numbers)

# print
print("{}".format('Hyunjae'))
print("{}".format(random_numbers[0]))
print("{}".format(random_numbers[1]))
print("Sum = {}".format(_sum))
print("Average = {}".format(_avg))
