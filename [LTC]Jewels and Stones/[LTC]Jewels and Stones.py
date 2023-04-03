#solution1

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dic= {}
        answer = 0
        for i in jewels:
            if i in dic:
                dic[i]+=1   
            else:
                    dic[i] = 1 

        for j in stones:
            if j in dic:    
                answer += dic[j]
        return(answer)
    
    
#solution2
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(map(jewels.count,stones))