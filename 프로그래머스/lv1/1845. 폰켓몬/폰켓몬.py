def select(nums):
    dic = {}
    for n in nums:
        if n in dic.keys():
            dic[n]+=1
        else:
            dic[n]=1
    print(dic)
    print(len(dic))
    if len(dic)>len(nums)/2:
        return len(nums)/2
    else:
        return len(dic)
    
def solution(nums):
    answer = 0

    answer = select(nums)
    return answer