def solution(sticker):
    def calculate(nums):
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        return dp[-1]
        
    # dp[i] = i를 때었을 때, 최댓값을 저장
    if len(sticker) == 1: return sticker[0]
    # 첫번째 스티커를 때냐 안 때냐
    ans = max(calculate(sticker[1:]),calculate(sticker[:-1]))
    
    return ans