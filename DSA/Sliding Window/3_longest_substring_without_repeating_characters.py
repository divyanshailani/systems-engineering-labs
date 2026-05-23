# Day 08: Longest Substring Without Repeating Characters (LeetCode 3)
# Focus: Variable Sliding Window / Substrings with unique characters.
# Submission Status: Accepted (11ms runtime, Beats 77.05%)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters.
        
        Time Complexity: O(N) - Each character is visited at most twice (by left and right pointers).
        Space Complexity: O(min(N, M)) - Where M is the size of the alphabet/charset (size of the set).
        """
        left = 0
        seen = set()
        max_len = 0
        
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len
                
        return max_len

# --- Mastery Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    test_cases = [
        ("abcabcbb", 3),             # Substring: "abc" (len 3)
        ("bbbbb", 1),                # Substring: "b" (len 1)
        ("pwwkew", 3),               # Substring: "wke" (len 3)
        ("", 0),                     # Empty string (len 0)
        (" ", 1),                    # Space string (len 1)
        ("dvdf", 3),                 # Substring: "vdf" (len 3) - Test left shift correctly
        ("abba", 2)                  # Substring: "ab" or "ba" (len 2)
    ]
    
    print("Testing Longest Substring Without Repeating Characters (LeetCode 3):")
    for s, expected in test_cases:
        result = sol.lengthOfLongestSubstring(s)
        print(f"s: {repr(s)} | Result: {result} | Expected: {expected}")
        assert result == expected
        
    print("\nAll tests passed successfully!")
