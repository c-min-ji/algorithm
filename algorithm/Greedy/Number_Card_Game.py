#for & min()을 사용하는 코드
def solution():
    N, M = map(int, input().split()) # 행, 열 입력 받음 cf. 행 = ㅡ, 열 = ㅣ

    result = 0 # 0으로 완전 최소값 설정하고 시작

    for i in range(N): # N개의 행만큼 반복
        data = list(map(int, input().split())) # 카드 리스트 입력 받음
        min_num = min(data) # 입력받은 data에서 최소값을 찾음
        result = max(result, min_num) # result와 min_num 중에 최대값을 찾음 ex) 0, 1 이면 1이 result가 됨 이렇게 N번 반복

    return result

print(solution())
