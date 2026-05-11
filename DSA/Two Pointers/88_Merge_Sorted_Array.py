class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Pattern 1: Two Pointers (Back-to-Front)
        Strategy: Fill nums1 from the end to avoid overwriting original data.
        Time Complexity: O(m + n)
        Space Complexity: O(1) - In-place modification
        """
        # p1: Pointer for the last actual element in nums1
        # p2: Pointer for the last element in nums2
        # w:  Writer pointer for the very end of nums1 (buffer)
        p1 = m - 1
        p2 = n - 1
        w = m + n - 1
        
        # Main comparison loop
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[w] = nums1[p1]
                p1 -= 1
            else:
                nums1[w] = nums2[p2]
                p2 -= 1
            w -= 1
            
        # Cleanup Crew: If nums2 still has leftovers (p1 leftovers are already in place)
        while p2 >= 0:
            nums1[w] = nums2[p2]
            p2 -= 1
            w -= 1

# Lab Note: Starting from the back is a common trick to achieve O(1) space 
# when you have a pre-allocated buffer at the end of an array.
