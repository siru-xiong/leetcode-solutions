# Problem Id:  1570
# Problem Name:  Dot Product of Two Sparse Vectors, 两个稀疏向量的点积
# Problem Url:  https://leetcode-cn.com/problems/dot-product-of-two-sparse-vectors/
# Problem Level:  Medium
 
class SparseVector:
    def __init__(self, nums: List[int]):
        self.coef = {}
        for j in range(len(nums)):
            if nums[j] != 0:
                self.coef[j] = nums[j]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for i in self.coef:
            for j in vec.coef:
                if i == j:
                    res += self.coef[i]*vec.coef[j]
        return res
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)