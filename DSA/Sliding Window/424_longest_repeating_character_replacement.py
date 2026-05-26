# Day 09: Longest Repeating Character Replacement (LeetCode 424)
# Focus: Variable Sliding Window / Character replacements to maximize contiguous segment.
# Submission Status: Ready for verification

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Finds the length of the longest substring containing the same letter 
        you can get after performing at most k character replacements.
        
        Time Complexity: O(N) - Single pass with two pointers. Each character is processed at most twice.
        Space Complexity: O(1) - The frequency map stores at most 26 uppercase English letters.
        """
        left = 0
        max_len = 0
        max_freq = 0
        window = {}
        
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            
            # Keep track of the maximum frequency of a single character in any window seen so far
            max_freq = max(max_freq, window[char])
            
            # Current window size is right - left + 1.
            # Number of replacements needed is: window_size - max_freq.
            # If this exceeds k, shrink the window from the left.
            while (right - left + 1) - max_freq > k:
                window[s[left]] -= 1
                left += 1
                
            # Update the max length of a valid window
            max_len = max(max_len, right - left + 1)
            
        return max_len

# --- Mastery Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    test_cases = [
        ("ABAB", 2, 4),          # Replace two 'A's with 'B's -> "BBBB" (len 4)
        ("AABABBA", 1, 4),       # Replace middle 'A' with 'B' -> "BBBB" (len 4)
        ("A", 0, 1),             # Single character, 0 replacements -> "A" (len 1)
        ("ABCDE", 1, 2),         # Replace any character to match its neighbor -> (len 2)
        ("AAAA", 2, 4),          # No replacements needed, already uniform -> (len 4)
        ("BAAAB", 2, 5),         # Replace both 'B's with 'A's -> "AAAAA" (len 5)
    ]
    
    print("Testing Longest Repeating Character Replacement (LeetCode 424):")
    for s, k, expected in test_cases:
        result = sol.characterReplacement(s, k)
        print(f"s: {repr(s)}, k: {k} | Result: {result} | Expected: {expected}")
        assert result == expected
        
    print("\nAll tests passed successfully!")
