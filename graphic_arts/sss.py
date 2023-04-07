nums = [0, 1, 2, 2, 3, 0, 4, 2]

val = 2
n = len(nums)

for i in range(n - 1):
    if nums[i] == val:
        for z in range(i + 1, n):
            if nums[z] != val:
                nums[i], nums[z] = nums[z], nums[i]
count = 0
for i in nums:
    if i == val:
        count += 1

print(count)
print(nums)
