# 좀 더 봅시다~ 이게 아마 규칙을 파악해서 쓰는 식인데 count부터 봅시당

def solution():
    n, m, k = map(int, input().split()) # n=num_list 개수, m=몇 번 더하는지, k=같은 수를 최대 몇 번 더할수있는지 input_ex) n, m, k = 5, 8, 3
    num_list = list(input().split()) # num_list=주어지는 수 input_ex) num_list = [2,4,5,4,6]
    
    num_list.sort() # 오름차순으로 정렬

    first_bNum = num_list[n-1] # 정렬 후 제일 큰 수를 찾음(정렬했으니까 제일 큰 수는 맨 뒤)
    second_bNum = num_list[n-2] # 정렬 후 두 번째 큰 수를 찾음(정렬했으니까 두 번째 큰 수는 맨 뒤에서 하나 앞)

    count = int(m/(k+1))*k # 숫자를 대입해 보면 더 쉽게 이해 가능. 패턴이 큰수를 K번 더하고 두번째로 작은 수를 한 번 더해주는 것! 그래서 K+1인데 이걸 M이랑 나뭐서 몫을 K번 반복해야하니까 곱한다! 
    #예를 들어서 M이 11이고 k가 4면 11/(5) * 5 => 2*10 앞에 2는 패턴이 몇번 반복되는 가를 알려줌!
    count += m%(k+1) # count에서 만약 k가 4이고 M이 11이면 애매하게 4번씩 반복을 못 할 수도 있는데 이때 m%(k+1) 식을 이용하면 1이 나온다. 그러면 큰 수를 1번 더 더할 수 있는 것!
    
    result = 0
    result += (count)*first_bNum #큰 수 * 큰 수 더할 수 있는 횟수
    result += (m-count)*second_bNum #두번째로 큰 수 * 두번째로 큰 수 더할 수 있는 횟수

    return(result)

print(solution()).
