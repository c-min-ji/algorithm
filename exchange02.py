def solution():
    n, m, k = map(int, input().split()) # n=num_list 개수, m=몇 번 더하는지, k=같은 수를 최대 몇 번 더할수있는지 input_ex) n, m, k = 5, 8, 3
    num_list = list(input().split()) # num_list=주어지는 수 input_ex) num_list = [2,4,5,4,6]
    
    num_list.sort() # 오름차순으로 정렬

    first_bNum = num_list[n-1] # 정렬 후 제일 큰 수를 찾음(정렬했으니까 제일 큰 수는 맨 뒤)
    second_bNum = num_list[n-2] # 정렬 후 두 번째 큰 수를 찾음(정렬했으니까 두 번째 큰 수는 맨 뒤에서 하나 앞)

    count = int(m/(k+1))*k
    count += m%(k+1)
    
    result = 0
    result += (count)*first_bNum
    result += (m-count)*second_bNum

    return(result)

print(solution())