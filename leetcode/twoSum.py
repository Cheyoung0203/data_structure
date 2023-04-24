# noinspection PyMethodMayBeStatic

class Solution:
    def two_sum(self, nums: list[int], target2: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target2:
                    return [i, j]


numbers = [2, 7, 11, 15]
target = 9


f = Solution()
res = f.two_sum(numbers, target)

print(res)
