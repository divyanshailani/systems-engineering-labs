# Day 06: Longest Substring with K Unique Characters (Variable Sliding Window)
# Focus: Dynamic window contraction using a frequency map to maintain exactly K distinct characters.
# Verification: Fits standard "Longest Substring with K Unique Characters" (GFG/LeetCode Premium 340 adaptation)
# Submission Status: Accepted (1120/1120 test cases, 100% accuracy, 0.05s runtime)

class Solution:
    def longestKSubstr(self, s: str, k: int) -> int:
        """
        Finds the length of the longest substring with EXACTLY k unique characters.
        If no such substring exists, returns -1.
        
        Time Complexity: O(N) - Each character is processed at most twice (by left/right pointers).
                         Hash map operations (insert/delete/lookup) are O(1) average.
        Space Complexity: O(K) - The hash map stores at most K + 1 unique characters at any time.
        """
        window = {}
        left = 0
        max_len = -1
        
        for right in range(len(s)):
            char = s[right]
            if char in window:
                window[char] += 1
            else:
                window[char] = 1
                
            # If we exceed K unique characters, shrink from the left
            while len(window) > k:
                leaving = s[left]
                window[leaving] -= 1
                if window[leaving] == 0:
                    del window[leaving]
                left += 1
                
            # Update the answer only when we have EXACTLY K unique characters
            if len(window) == k:
                current_len = right - left + 1
                if current_len > max_len:
                    max_len = current_len
                    
        return max_len

    def longestAtMostKSubstr(self, s: str, k: int) -> int:
        """
        Finds the length of the longest substring with AT MOST k unique characters.
        (LeetCode 340: Longest Substring with At Most K Distinct Characters)
        
        Time Complexity: O(N)
        Space Complexity: O(K)
        """
        if not s or k <= 0:
            return 0
            
        window = {}
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            char = s[right]
            if char in window:
                window[char] += 1
            else:
                window[char] = 1
                
            while len(window) > k:
                leaving = s[left]
                window[leaving] -= 1
                if window[leaving] == 0:
                    del window[leaving]
                left += 1
                
            # For AT MOST K, any window size <= K is valid
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len
            
        return max_len

# --- Mastery Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # 1. Testing EXACTLY K Uniques
    exact_test_cases = [
        ("aabacbebebe", 3, 7),  # "cbebebe" has 'c', 'b', 'e' and length 7
        ("aaaa", 2, -1),        # Only 1 unique char 'a', impossible to get exactly 2
        ("eceba", 3, 4),        # "eceb" has 'e', 'c', 'b' and length 4
        ("aba", 4, -1),         # len(s) < K, impossible
        ("abaccc", 2, 4)        # "accc" has exactly 2 uniques (a,c) and length 4
    ]
    
    print("Testing Longest Substring with EXACTLY K Unique Characters:")
    for s, k, expected in exact_test_cases:
        result = sol.longestKSubstr(s, k)
        print(f"s: '{s}', k: {k} | Result: {result} | Expected: {expected}")
        assert result == expected
    print("All EXACTLY K tests passed!\n")
    
    # 2. Testing AT MOST K Uniques (LeetCode 340 variant)
    at_most_test_cases = [
        ("eceba", 2, 3),        # "ece" has at most 2 uniques and length 3
        ("aa", 1, 2),           # "aa" has 1 unique and length 2
        ("aabacbebebe", 3, 7),  # "cbebebe" has 3 uniques and length 7
        ("a", 0, 0),            # k = 0, impossible to have chars
        ("abaccc", 2, 4)        # "accc" has 2 uniques and length 4
    ]
    
    print("Testing Longest Substring with AT MOST K Unique Characters:")
    for s, k, expected in at_most_test_cases:
        result = sol.longestAtMostKSubstr(s, k)
        print(f"s: '{s}', k: {k} | Result: {result} | Expected: {expected}")
        assert result == expected
    print("All AT MOST K tests passed!\n")
