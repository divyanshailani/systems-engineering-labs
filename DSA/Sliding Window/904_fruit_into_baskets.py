# Day 07: Fruit Into Baskets (LeetCode 904)
# Focus: Variable Sliding Window / Equivalent to Longest Subarray with At Most 2 Unique Elements (K = 2).
# Submission Status: Accepted (0ms runtime)

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        """
        Finds the maximum number of fruits you can pick with only 2 baskets (at most 2 unique types of fruit).
        
        Time Complexity: O(N) - Each element is processed at most twice (by left/right pointers).
                         Hash map operations (insert/delete/lookup) are O(1).
        Space Complexity: O(1) - The hash map stores at most 3 unique keys (K + 1) at any time.
        """
        left = 0
        window = {}
        max_fruits = 0
        
        for right in range(len(fruits)):
            fruit_type = fruits[right]
            
            # Slide window right: include current fruit in map
            if fruit_type in window:
                window[fruit_type] += 1
            else:
                window[fruit_type] = 1
                
            # If we have more than 2 distinct types of fruit, shrink the window from the left
            while len(window) > 2:
                leaving = fruits[left]
                window[leaving] -= 1
                if window[leaving] == 0:
                    del window[leaving]
                left += 1
                
            # For "at most 2 uniques", the current window [left, right] is always valid here.
            current_len = right - left + 1
            if current_len > max_fruits:
                max_fruits = current_len
                
        return max_fruits

# --- Mastery Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    test_cases = [
        ([1, 2, 1], 3),             # Subarray: [1, 2, 1] (len 3)
        ([0, 1, 2, 2], 3),          # Subarray: [1, 2, 2] (len 3)
        ([1, 2, 3, 2, 2], 4),       # Subarray: [2, 3, 2, 2] (len 4)
        ([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4], 5), # Subarray: [1, 2, 1, 1, 2] (len 5)
        ([0], 1),                   # Subarray: [0] (len 1)
        ([], 0)                     # Empty array (len 0)
    ]
    
    print("Testing Fruit Into Baskets (LeetCode 904):")
    for fruits, expected in test_cases:
        result = sol.totalFruit(fruits)
        print(f"fruits: {fruits} | Result: {result} | Expected: {expected}")
        assert result == expected
        
    print("\nAll tests passed successfully!")
