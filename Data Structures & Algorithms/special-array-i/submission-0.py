class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        parity = "even" if nums[0] % 2 == 0 else "odd"

        for i in range(1, len(nums)):
            if nums[i] % 2 == 0:
                if parity == "even":
                    return False
                else:
                    parity = "even"
            
            else:
                if parity == "odd":
                    return False
                else:
                    parity = "odd"
        
        return True