class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1



class Solution:

  def sortColors(self, nums: list[int]) -> None:
    """Do not return anything, modify nums in-place instead."""
    count0 = 0
    count1 = 0
    count2 = 0

    # Pass 1: Count 0s
    for num in nums:
      if num == 0:
        count0 += 1

    # Pass 2: Count 1s
    for num in nums:
      if num == 1:
        count1 += 1

    # Pass 3: Count 2s
    for num in nums:
      if num == 2:
        count2 += 1

    # Overwrite the original array in-place
    idx = 0
    for _ in range(count0):
      nums[idx] = 0
      idx += 1

    for _ in range(count1):
      nums[idx] = 1
      idx += 1

    for _ in range(count2):
      nums[idx] = 2
      idx += 1