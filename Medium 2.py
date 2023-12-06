def ele(nums):
    if not nums:
        return []
    
    c1,c2,count1,count2=None,None,0,0

    for num in nums:
        if num==c1:count1 += 1
        elif num==c2: count2 += 1
        elif count1 == 0: c1,count1=num,1
        elif count2 == 0: c2,count2=num,1
        else:count1,count2=count1-1,count2-1

        count1,count2=nums.count(c1),nms.count(c2)
        result=[candidate for candidate,count in [(c1,count1),(c2,count2)] if count > len(nums) // 3]

        return result
    
user_input=input()
nums=list(map(int,user_input[1:-1].split(',')))

output=else(nums)
print(output)