def solution(my_string, overwrite_string, s):
    
    
    answer = ''

    for i in range(0,len(my_string)):
        if i>=s and i<=(s+len(overwrite_string)-1):
            # print(len(overwrite_string))
            answer += overwrite_string[i-s]
    
        else:
            answer += my_string[i]
        
    return answer


print(solution("He11oWor1d",	"lloWorl",	2))