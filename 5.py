def solution(start_num, end_num):
    answer = []
    for i in range(start_num - end_num):
        answer.append(start_num-i)
    return answer

print(solution(10,3))