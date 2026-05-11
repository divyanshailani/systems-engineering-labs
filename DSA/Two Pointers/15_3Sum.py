class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        Pattern 1: Two Pointers (The Boss Battle)
        Strategy: Sort, fix one number (i), and use Two Sum II logic for the remaining two.
        Key Mechanic: Rigorous duplicate skipping for both the fixed number and the scouts.
        Time Complexity: O(n^2) - Outer loop * Inner Two-Pointer loop
        Space Complexity: O(1) or O(n) depending on sorting algorithm memory.
        """
        nums.sort()
        result = []
        
        for i in range(len(nums)):
            # Rule 1: Skip duplicate 'fixed' numbers to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # Rule 2: Skip duplicate 'scout' numbers after finding a match
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1
                    
        return result

# Lab Note: 3Sum is simply a nested "Two Sum II". The complexity comes from
# managing the bounds and skipping duplicates to satisfy the set constraint.
