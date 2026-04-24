nums = [3,0,1]

n = len(nums)
expected = n * (n + 1) // 2
actual = sum(nums)

print("Missing:", expected - actual)
