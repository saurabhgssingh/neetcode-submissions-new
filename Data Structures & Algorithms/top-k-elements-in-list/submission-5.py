class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        val_dict = {}
        bucket = [[] for _ in range(len(nums) + 1)]
        for v in nums:
            val_dict[v] = val_dict.get(v,0) + 1

        for key,val in val_dict.items():
            bucket[val]=bucket[val]+[key]
        
        op = []
        # print(bucket)
        for i in range(len(nums),0,-1):
            for item in bucket[i]:
                op.append(item)
                if len(op)==k:
                    return op
            
        

        

        