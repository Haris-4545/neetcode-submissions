class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seendigits = {}

        for i, number in enumerate(nums):
            complement = target - number
            if complement in seendigits:
                return[seendigits[complement], i]
            seendigits[number] = i
        return []
