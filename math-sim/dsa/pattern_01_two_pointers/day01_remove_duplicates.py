# Day 01: Remove Duplicates from Sorted Array (Two Pointers - Fast/Slow)
# Focus: In-place array modification and memory efficiency.

def removeDuplicates(nums: list[int]) -> int:
    """
    Removes duplicates in-place from a sorted array.
    Returns the count of unique elements (k).
    Time Complexity: O(n) - Single pass through the array.
    Space Complexity: O(1) - Modifies the array in-place.
    """
    if not nums:
        return 0
        
    # 'left' is the 'Writing' pointer (tracks the last unique element)
    # 'right' is the 'Scout' pointer (scans for new unique values)
    left = 0
    
    for right in range(1, len(nums)):
        # If scout finds a value different from the last unique value
        if nums[left] != nums[right]:
            # Move the writer forward and copy the new unique value
            left += 1
            nums[left] = nums[right]
            
    # Number of unique elements is the final index + 1
    return left + 1

# --- Mastery Test Cases ---
if __name__ == "__main__":
    test_cases = [
        ([1, 1, 2], 2, [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4])
    ]
    
    for nums, expected_k, expected_nums in test_cases:
        original_nums = list(nums)
        k = removeDuplicates(nums)
        print(f"Input: {original_nums} | k: {k} | Array: {nums[:k]}")
        assert k == expected_k
        assert nums[:k] == expected_nums
