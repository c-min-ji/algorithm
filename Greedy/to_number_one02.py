def solution():
    n, k = map(int, input().split())
    result = 0

    while True: #무한반복
        target = (n//k)*k #몫에 k곱하기
        result += (n-target) #n에서 target뺀거를 result에 더하기
        n = target

        if n<k: #위 과정을 거쳐서 k가 n보다 크면 while문 종료
            break

        result += 1
        n//=k

    result += (n-1)
    return result

print(solution())
