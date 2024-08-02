'''
3번 문제
정수배열 nums와 정수 k, t 가 주어졌을때 아래 조건을 만족하면 임의의 서로다른 정수 i,j가 존재하면  True, 아니면 False

조건

abs(nums[i] - nums[j]) <= t 
abs(i-j) <= k 

0 < nums.length() < 10**5+1
0< nums[i] < 10**5+1(수정됨
'''

def answer(nums, k, t):
    if k < 1 or t < 0:
        return False

    width = t + 1
    bucket = {}
    
    for i, num in enumerate(nums):
        bucket_id = num // width
        
        if bucket_id in bucket:
            return True
        
        if bucket_id - 1 in bucket and abs(num - bucket[bucket_id - 1]) < width:
            return True
        
        if bucket_id + 1 in bucket and abs(num - bucket[bucket_id + 1]) < width:
            return True
        
        bucket[bucket_id] = num
        
        if i >= k:
            del bucket[nums[i - k] // width]
    
    return False


# nums = [1, 5, 9, 13]
# k = 2 
# t = 4
nums = [1, 10, 20, 30]
k = 1 
t = 5 
print(answer(nums, k, t))
