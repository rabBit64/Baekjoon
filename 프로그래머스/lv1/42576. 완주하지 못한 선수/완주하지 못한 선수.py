import collections
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    result = collections.Counter(participant)-collections.Counter(completion)
    #print(list(result)[0])
    answer = list(result)[0]
    return answer