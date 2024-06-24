class Solution:
    # One pass hashmap O(n)
    @staticmethod
    def two_sum(nums: [int], target: int) -> [int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i

    # Two pass hash map
    @staticmethod
    def two_sum2(nums:[int], target: int) -> [int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
            for i in range(len(nums)):
                complement = target - nums[i]
                if complement in hashmap and hashmap[complement] != i:
                    return [i, hashmap[complement]]

    # Big O(n^2) Brute Force
    @staticmethod
    def two_sum3(nums:[int], target: int) -> [int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]