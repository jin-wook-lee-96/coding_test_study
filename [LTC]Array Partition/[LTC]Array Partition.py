class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        result = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            result += min(nums[i],nums[i+1])
        return result

#sort안쓰고 실패한 풀이(수정필요) 
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        arr = 0
        result = []
        for j in range(len(nums)):
            result.append(heapq.heappop(nums))
        for i in range(0, len(result), 2): 
            arr += min(result[i],result[i+1])
        return arr
