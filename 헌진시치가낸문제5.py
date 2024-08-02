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
