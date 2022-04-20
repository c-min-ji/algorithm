def solution(food_times, k):
    if sum(food_times)<=k:
        return -1
      
    import heapq
    
    heap = []
    for i in range(len(food_times)):
        heapq.heappush(heap, (food_times[i], i+1))
        
    sum_time = 0
    pre = 0
    food = len(food_times)
    
    while sum_time + ((heap[0][0] - pre) * food) <= k:
        curr = heapq.heappop(heap)[0]
        sum_time += (curr-pre) * food
        food -= 1
        pre = curr
    
    answer = sorted(heap, key=lambda x: x[1])
    return answer[(k-sum_time)%food][1]
