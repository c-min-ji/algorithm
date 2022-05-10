def solution():
    N, K = map(int, input().split())
    count = 0

    while N>=K:
        while N%K !=0: #N이 K로 나누어 떨어질 때까지 -1해줌
            N -= 1
            count += 1
        
        N //= K #나누어지면 나눔
        count += 1
    
    while N>1:
        N -= 1
        count += 1

    return count

print(solution())
