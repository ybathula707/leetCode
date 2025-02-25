class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        nums1NonZeroEndIdx = m - 1
        nums2EndIdx = n - 1

        for endResArr in range(n + m - 1, -1, -1):
            if nums2EndIdx < 0:
                break
            if (
                nums1NonZeroEndIdx >= 0
                and nums1[nums1NonZeroEndIdx] > nums2[nums2EndIdx]
            ):
                nums1[endResArr] = nums1[nums1NonZeroEndIdx]
                nums1NonZeroEndIdx -= 1
            else:
                nums1[endResArr] = nums2[nums2EndIdx]
                nums2EndIdx -= 1
