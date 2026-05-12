class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        # 1. Sort the array to enable two-pointer directional search
        nums.sort()
        # 2. Initialize with the first possible triplet sum
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # 3. Update the global "best seen so far" if current is closer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # 4. Standard Two-Pointer movement
                if current_sum == target:
                    return target # Perfect match
                elif current_sum < target:
                    left += 1     # Need a bigger sum
                else:
                    right -= 1    # Need a smaller sum
        
        # 5. Return the memory of the closest sum found
        return closest_sum
