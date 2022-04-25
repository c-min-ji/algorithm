def possible(answer):
    for x,y, s in answer:
        if s == 0:
            if y == 0 or [x-1, y, 1] in answer or [x,y,1] in answer or [x, y -1, 0] in answer:
                continue
            return False
        elif s == 1:
            if [x,y-1,0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for f in build_frame:
        x,y,s, oper = f
        if oper == 0:
            answer.remove([x,y,s])
            if not possible(answer):
                answer.append([x,y,s])
        if oper == 1:
            answer.append([x,y,s])
            if not possible(answer):
                answer.remove([x,y,s])
                
    return sorted(answer)
