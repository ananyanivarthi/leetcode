class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap=[(val,idx) for idx,val in enumerate(nums)]
        heapq.heapify(heap)
        for _ in range(k):
            smallest,idx=heapq.heappop(heap)
            updated_val=smallest*multiplier
            heapq.heappush(heap,(updated_val,idx))
        
        result=[0]*len(nums)
        for value,idx in heap:
            result[idx]=value
        return result