from collections import deque

def maxSliding(nums,k):
    result=[]
    window=deque()

    for i in range(len(nums)):
        while window and window[0]<i-k+1:
            window.popleft()

        while window and nums[window[-1]] < nums[i]:
            window.pop()

        window.append(i)

        if i >= k-1:
            result.append(nums[window[0]])

    return result

nums_str=input()
k=int(input())

nums=[int(x) for x in nums_str.strip('[]').split(',')]

result=maxSliding(nums,k)
print(result)