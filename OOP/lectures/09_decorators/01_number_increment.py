def number_increment(nums):
    def increase():
        result = [n + 1 for n in nums]
        return result
    return increase()


print(number_increment([1, 2, 3]))
