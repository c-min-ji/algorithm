def solution():
    n, m, k = map(int, input().split()) # n=num_list 개수, m=몇 번 더하는지, k=같은 수를 최대 몇 번 더할수있는지 input_ex) n, m, k = 5, 8, 3
    num_list = list(input().split()) # num_list=주어지는 수 input_ex) num_list = [2,4,5,4,6]
    
    num_list.sort() # 오름차순으로 정렬 내림차순하려면 reverse=True

    first_bNum = num_list[n-1] # 정렬 후 제일 큰 수를 찾음(정렬했으니까 제일 큰 수는 맨 뒤)
    second_bNum = num_list[n-2] # 정렬 후 두 번째 큰 수를 찾음(정렬했으니까 두 번째 큰 수는 맨 뒤에서 하나 앞)

    result = 0 # 총 더한 값 (=sum)

    while True: # m이 0이 될 때까지 무한으로 반복
        for i in range(k): # k번 더할수 있으니까 range(k)
            if m == 0: # 0이면 while문 끝내
                break
            result += first_bNum # 아니면 result에 첫 번째 큰 수를 더함
            m -= 1 # 횟수 한 번 차감
        if m == 0: # 위에 첫 번째 큰 수 더하고 m=0이면 while문 끝내
            break
        result += second_bNum # result에 두 번째 큰 수 더함
        m -= 1 # 횟수 차감
    
    return result #def의 리턴 값

print(solution()) # 출력
