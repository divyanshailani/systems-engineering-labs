# Day 01: Two Sum II - Input Array Is Sorted (Two Pointers Pattern)
# Focus: Exploiting sorted properties for O(n) search.

def twoSum(numbers: list[int], target: int) -> list[int]:
    """
    Finds two numbers such that they add up to a specific target.
    Input array is already sorted.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            # Problem asks for 1-based indexing
            return [left + 1, right + 1]
        elif current_sum < target:
            # Sum is too small, move left pointer forward to increase it
            left += 1
        else:
            # Sum is too large, move right pointer backward to decrease it
            right -= 1
            
    return []

# --- Mastery Test Cases ---
if __name__ == "__main__":
    test_cases = [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2])
    ]
    
    for nums, target, expected in test_cases:
        result = twoSum(nums, target)
        print(f"Nums: {nums} | Target: {target} | Result: {result} | Expected: {expected}")
        assert result == expected
