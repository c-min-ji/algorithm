# 2중 for문 사용

def solution():
    N, M = map(int, input().split())

    result = 0

    for i in range(N):
        data = list(map(int, input().split()))

        min_num = 10001 #최대 입력 가능 수가 10000이니까 100001을 최소값으로 잡고 시작

        for j in data: # for j in range(data)-->안됨....주의! 그냥 in data임
            min_num = min(min_num, j) # 이 중에 가장 작은 거 우선 고르기

        result = max(min_num, result) # 그리고 그 중에서 최대값 찾기
    
    return result

print(solution())