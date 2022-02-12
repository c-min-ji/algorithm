 def solution(s):
    answer = len(s)
    for i in range(1, (len(s)//2)+1):
        cut = ""
        pre = s[0:i]
        cnt = 1
        for j in range (i, len(s), i): #i만큼 넘어감
            if pre == s[j:j+i]: #이전 값이 다음 값이랑 같으면
                cnt += 1 #cnt + 1
            else: #이전 값이 다음 값이랑 다르면
                if cnt >= 2: #cnt(중복된 값)이 두개 이상이면 반복되는 문자열 앞에 숫자 붙여줌
                    cut += str(cnt)+pre
                else: #아니면 그냥 문자열만
                    cut += pre
                pre = s[j:j+i] #pre값을 현재 값으로 업데이트
                cnt = 1 #cnt 초기화
        if cnt>=2:
            cut += str(cnt)+pre
        else:
            cut += pre
        answer = min(answer, len(cut)) #둘 중 작은 거 출력
    return answer
