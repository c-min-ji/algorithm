# 좀 더 봅시다~ 이게 아마 규칙을 파악해서 쓰는 식인데 count부터 봅시당

def solution():
    n, m, k = map(int, input().split()) # n=num_list 개수, m=몇 번 더하는지, k=같은 수를 최대 몇 번 더할수있는지 input_ex) n, m, k = 5, 8, 3
    num_list = list(input().split()) # num_list=주어지는 수 input_ex) num_list = [2,4,5,4,6]
    
    num_list.sort() # 오름차순으로 정렬

    first_bNum = num_list[n-1] # 정렬 후 제일 큰 수를 찾음(정렬했으니까 제일 큰 수는 맨 뒤)
    second_bNum = num_list[n-2] # 정렬 후 두 번째 큰 수를 찾음(정렬했으니까 두 번째 큰 수는 맨 뒤에서 하나 앞)

    count = int(m/(k+1))*k # 숫자를 대입해 보면 더 쉽게 이해 가능. 
    #같은 수를 반복해서 더할 수 있는 횟수 k 에 그 다음 작은 수를 더하니까 +1을 해준다. 그리고 총 더하는 횟수인 m이랑 나눠서 몫을 구한다. 여기에 k를 곱한다.. ?
    count += m%(k+1) # count에 나머지를 더한다..?아 나눠떨어지지않는 경우의 수다...
    
    result = 0
    result += (count)*first_bNum
    result += (m-count)*second_bNum

    return(result)

print(solution())
