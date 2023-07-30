def solution(participant, completion):
    answer = ''
    dic = {}
    for name in participant:
        if name not in dic:
            dic[name]=1
        else:
            dic[name]+=1
    #print(dic)
    for name in completion:
        dic[name]-=1
    #print(dic)
    for key,value in dic.items():
        if value>0:
            answer=key
    return answer