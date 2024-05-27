import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
   
    while True:
        if scoville[0]>=K:
            break
        else:
            answer+=1
            a=heapq.heappop(scoville)
            b=heapq.heappop(scoville)
            heapq.heappush(scoville,a+b*2)
            if len(scoville)==1 and scoville[0]<K:
                return -1

    return answer