class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        # odd case
        if (n1 + n2) % 2 == 1:
            return self.kth(nums1, nums2, (n1 + n2) // 2)
        # even case
        else:
            mid1 = self.kth(nums1, nums2, (n1 + n2) // 2 - 1)
            mid2 = self.kth(nums1, nums2, (n1 + n2) // 2)
            return (mid1 + mid2) / 2

    # kth aims to find the kth smallest number of 2 sorted arrays
    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        # index of mid element
        ia, ib = len(a) // 2, len(b) // 2
        # value of mid element
        va, vb = a[ia], b[ib]
        # if k is larger than ia + ib
        if ia + ib < k:
            # if va > vb, then b's first half doesn't include k
            if va > vb:
                return self.kth(a, b[ib+1:], k - ib - 1)
            # if va <= vb, then a's first half doesn't include k
            elif va <= vb:
                return self.kth(a[ia+1:], b, k - ia - 1)
        # if k is larger than ia + ib
        elif ia + ib >= k:
            # if va > vb, then a's last half doesn't include k
            if va > vb:
                return self.kth(a[:ia], b, k)
            # if va <= vb, then a's last half doesn't include k
            elif va <= vb:
                return self.kth(a, b[:ib], k)

    '''
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # length of 2 arrays
        n1 = len(nums1)
        n2 = len(nums2)
        mid = n1 + n2 / 2
        # aggregate array
        n = []
        # index
        i = 0
        j = 0
        # combine
        while i < n1 and j < n2:
            if nums1[i] <= nums2[j]:
                n.append(nums1[i])
                i += 1
            else:
                n.append(nums2[j])
                j += 1
        if i <= n1-1:
            n.extend(nums1[i:])
        else:
            n.extend(nums2[j:])
        # find the median
        if (n1 + n2) % 2 == 1:
            idx = (n1 + n2 - 1) // 2
            return n[idx]
        else:
            idx1 = (n1 + n2) // 2 - 1
            idx2 = idx1 + 1
            return (n[idx1] + n[idx2]) / 2
    '''

