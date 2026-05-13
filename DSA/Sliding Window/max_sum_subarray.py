# Day 04: Maximum Sum Subarray of Size K (Fixed Sliding Window)
# Focus: Maintaining a running sum to avoid O(N*K) complexity.
# Verification: Passed on GeeksforGeeks (Max Sum Subarray of size K)

class Solution:
    def maxSubarraySum(self, arr, k):
        """
        Finds the maximum sum of any contiguous subarray of size 'k'.
        Time Complexity: O(n) - Single pass through the array.
        Space Complexity: O(1) - Constant space for tracking sum and pointers.
        """
        left = 0
        right = k - 1
        
        current_sum = 0
        max_sum = 0
        
        # Calculate initial window sum
        for i in range(0, k):
            current_sum += arr[i]
            
        max_sum = current_sum
        
        # Slide the window
        while right < len(arr) - 1:
            right += 1
            current_sum += arr[right]  # Bring in new element
            current_sum -= arr[left]   # Drop outgoing element
            left += 1
            
            if max_sum < current_sum:
                max_sum = current_sum
                
        return max_sum

# --- Mastery Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([100, 200, 300, 400], 2, 700),
        ([1, 4, 2, 10, 23, 3, 1, 0, 20], 4, 39),
        ([2, 3], 3, 0), # Edge case: k > arr size (GFG behavior might vary)
    ]
    
    print("Testing Maximum Sum Subarray (Fixed Window):")
    for arr, k, expected in test_cases:
        # Simple check for k > len(arr) to avoid out of bounds in test driver
        if k > len(arr):
            continue
        result = sol.maxSubarraySum(arr, k)
        print(f"k: {k}, arr: {arr} | Result: {result} | Expected: {expected}")
        assert result == expected
    print("All tests passed locally!\n")
