import math

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        """
        Time Complexity: O(n^2) - Sorting takes O(n log n), and the nested loops take O(n^2).
        Space Complexity: O(1) or O(n) depending on the sorting implementation.
        """
        nums.sort()
        n = len(nums)
        # Initialize with the first possible sum
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            # Optimization: Skip duplicate starters (though not strictly required for this problem)
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If we hit the target exactly, we can't get any closer
                if current_sum == target:
                    return current_sum
                
                # Update closest_sum if current_sum is closer to target
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum
                
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum

# Example Usage (for local testing):
# sol = Solution()
# print(sol.threeSumClosest([-1, 2, 1, -4], 1)) # Output: 2
