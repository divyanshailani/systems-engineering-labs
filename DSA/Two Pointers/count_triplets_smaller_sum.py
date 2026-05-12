class Solution:
    def countTriplets(self, target_sum: int, arr: list[int]) -> int:
        """
        Problem: Find count of triplets (i, j, k) with sum smaller than target_sum.
        Pattern: Two Pointers (with Bulk Counting)
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        arr.sort()
        count = 0
        n = len(arr)
        
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = arr[i] + arr[left] + arr[right]
                
                if current_sum < target_sum:
                    # THE GRASP: If sum is valid with arr[right], it's valid for 
                    # all elements between left and right because they are smaller.
                    count += (right - left)
                    left += 1
                else:
                    # Sum is too large, need to reduce it by moving the right pointer
                    right -= 1
                    
        return count
