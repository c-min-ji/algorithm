def solution():
    n = 1260 # 거슬러줄돈
    count = 0 # 동전 개수

    coin_type = [500, 100, 50, 10] # 동전 종류 넣어주기

    for coin in coin_type: # coin_type별로 for문 돔
        count += n//coin # 동전 개수에 동전 종류와 거스름돈을 나눈 몫을 더해줌  n/coin도 가능
        n %= coin # n은 이제 위에서 몫으로 나온 돈을 빼고 남은 돈이 됨
    
    return count # 몇 개의 동전을 받았는 지 return함
    
print(solution()) # 출력
