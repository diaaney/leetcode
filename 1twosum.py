nums = [2, 7, 11, 15]
target = 26

def two_sum(nums, target):
    seen = {}
    for index, number in enumerate(nums):
        missing = target - number
        if missing in seen:
            return (seen[missing], index)
        seen[number] = index
    return None

result = two_sum(nums, target)
print(result)