class Solution:
    def subarraySum(self, nums, k):
        frequency = defaultdict(int)
        frequency[0] = 1

        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num

            count += frequency[prefix_sum - k]
            frequency[prefix_sum] += 1

        return count