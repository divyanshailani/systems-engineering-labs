class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Problem: Sort an array of 0s, 1s, and 2s in-place (Dutch National Flag).
        Pattern: Three Pointers / Partitioning
        Time Complexity: O(n) - Single pass
        Space Complexity: O(1)
        """
        # Boundary pointers
        left = 0           # Boundary for 0s
        mid = 0            # Current explorer
        right = len(nums) - 1 # Boundary for 2s
        
        while mid <= right:
            if nums[mid] == 0:
                # Found a 0: swap it to the left boundary
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 1:
                # Found a 1: it's in the right zone, just move on
                mid += 1
            else: # nums[mid] == 2
                # Found a 2: swap it to the right boundary
                nums[mid], nums[right] = nums[right], nums[mid]
                # CRITICAL: Do not increment mid, we need to check the 
                # new element swapped from the end in the next iteration.
                right -= 1
        
        # In-place modification, no return needed.
