# Day 01: Valid Palindrome (Two Pointers Pattern)
# Focus: Efficient linear search with junk-skipping logic.

def isPalindrome(s: str) -> bool:
    """
    Checks if a string is a palindrome, ignoring non-alphanumeric characters.
    Time Complexity: O(n) - Single pass through the string.
    Space Complexity: O(1) - Constant space used for pointers.
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        # 'Fast-Forward' pointers past non-alphanumeric characters (junk)
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
            
        # Compare normalized characters
        if s[left].lower() == s[right].lower():
            left += 1
            right -= 1
        else:
            # Mismatch found: string is not a palindrome
            return False
            
    # If the pointers meet/cross without finding a mismatch, it's a palindrome
    return True

# --- Mastery Test Cases ---
if __name__ == "__main__":
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        (".,", True)
    ]
    
    for string, expected in test_cases:
        result = isPalindrome(string)
        print(f"Input: '{string}' | Result: {result} | Expected: {expected}")
        assert result == expected
