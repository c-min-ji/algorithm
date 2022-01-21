#n 값이 클 떄 유리
def solution():
    n, k = map(int, input().split())
    result = 0

    while True: #무한반복
        target = (n//k)*k #몫에 k곱하기
        result += (n-target) #n에서 target뺀거를 result에 더하기
        n = target #n을 계속 업데이트함

        if n<k: #위 과정을 거쳐서 k가 n보다 크면 while문 종료
            break

        result += 1 #k에 횟수 1 더하기
        n//=k 

    result += (n-1) #마지막 남은 수 1씩 빼기
    return result

print(solution())
