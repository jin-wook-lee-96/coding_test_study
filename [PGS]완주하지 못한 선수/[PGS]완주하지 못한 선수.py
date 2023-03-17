#olution1
def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for a,b in zip(participant, completion):
        if a != b:
            return a
    return participant[-1]

#solution2
def solution(participant, completion):
    dic = {}
    for name in participant:
        dic[name] = dic.get(name, 0) + 1
    for name in completion:
        dic[name] -= 1
    answer = [k for k, v in dic.items() if v > 0]
    return answer[0]
        