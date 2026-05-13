# Day 04: Minimum Size Subarray Sum (Variable Sliding Window)
# Focus: Dynamic window resizing (Expansion/Contraction) to find minimal length.
# Verification: Passed LeetCode 209 (Medium)

import math

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        """
        Finds the minimal length of a contiguous subarray whose sum is >= target.
        Time Complexity: O(n) - Each element is visited at most twice (by left/right pointers).
        Space Complexity: O(1) - Only constant space used for pointers and sum.
        """
        left = 0
        current_sum = 0
        min_length = float('inf')
        
        # Expand the window using the 'right' pointer
        for right in range(len(nums)):
            current_sum += nums[right]
            
            # Shrink the window as much as possible while sum >= target
            while current_sum >= target:
                # Update minimal length found so far
                # Formula: right - left + 1 accounts for 0-based indexing
                length = right - left + 1
                min_length = min(min_length, length)
                
                # Remove the leftmost element and move the 'left' pointer
                current_sum -= nums[left]
                left += 1
                
        # Return 0 if no valid subarray was found
        return min_length if min_length != float('inf') else 0

# --- Mastery Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        (7, [2, 3, 1, 2, 4, 3], 2),  # [4, 3] is the smallest
        (4, [1, 4, 4], 1),           # [4] is the smallest
        (11, [1, 1, 1, 1, 1, 1, 1, 1], 0), # No subarray >= 11
        (7, [2, 1, 5, 2, 3, 2], 2)   # [5, 2] is the smallest
    ]
    
    print("Testing Minimum Size Subarray Sum (Variable Window):")
    for target, nums, expected in test_cases:
        result = sol.minSubArrayLen(target, nums)
        print(f"target: {target}, nums: {nums} | Result: {result} | Expected: {expected}")
        assert result == expected
    print("All tests passed locally!\n")
