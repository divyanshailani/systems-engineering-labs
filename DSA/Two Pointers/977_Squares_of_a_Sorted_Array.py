class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        """
        Pattern 1: Two Pointers (Meeting in the Middle)
        Strategy: Compare squares at ends and fill result array from back to front.
        Time Complexity: O(n)
        Space Complexity: O(n) for result array
        """
        left = 0
        right = len(nums) - 1
        
        result = [0] * len(nums)
        writer = len(result) - 1
        
        while left <= right:
            left_sq = nums[left] * nums[left]
            right_sq = nums[right] * nums[right]
            
            # Since the array is sorted, the largest square must be at one of the ends
            if left_sq > right_sq:
                result[writer] = left_sq
                left += 1
            else:
                # Handles both right_sq > left_sq and right_sq == left_sq
                result[writer] = right_sq
                right -= 1
            
            writer -= 1
            
        return result

# Lab Note: This is an O(n) alternative to the O(n log n) sorting approach.
# It exploits the sorted nature of the input to find extremes in constant time.
