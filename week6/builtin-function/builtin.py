nums = [int(x) for x in input().split()]
a = 1
for x in range(len(nums)):
    a *= nums[x]
z = f'print({a})'
print(nums)
eval(z)