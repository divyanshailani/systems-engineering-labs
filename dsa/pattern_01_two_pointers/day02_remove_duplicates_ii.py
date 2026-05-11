class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        Pattern 1: Two Pointers (Scout & Writer)
        Strategy: Compare Scout with Writer-2 to allow at most 2 duplicates.
        Time Complexity: O(n) - Single pass
        Space Complexity: O(1) - In-place modification
        """
        if len(nums) <= 2:
            return len(nums)
        
        left = 2   # The Writer (gatekeeper)
        right = 2  # The Scout (explorer)
        
        while right < len(nums):
            # If the current number is different from the number 2 spots behind our 'valid' pointer
            if nums[right] != nums[left - 2]:
                nums[left] = nums[right]
                left += 1
            
            right += 1
            
        return left

# Lab Note: This is a 'Two Pointers' pattern with a K-step lookback.
# For 'at most K duplicates', change the index to 'left - K'.
