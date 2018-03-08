import copy

def test(temp):
	temp.append(44)


nums = [11, 22, 33]
print(nums)
# test(copy.deepcopy(nums))
test(nums[:])
print(nums)