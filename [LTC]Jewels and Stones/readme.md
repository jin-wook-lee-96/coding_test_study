# [문제링크](https://leetcode.com/problems/jewels-and-stones/description/)

## 문제
보석의 종류를 나타내는 줄 보석과 보유한 스톤을 나타내는 스톤이 주어집니다.
스톤의 각 문자는 내가 가진 스톤의 종류를 나타냅니다. 
내가 가진 스톤 중 몇 개가 보석인지 알고 싶을 것입니다.

문자는 대소문자를 구분하므로 "a"는 "A"와는 다른 종류의 스톤으로 간주됩니다.


ex1

    Input: jewels = "aA", stones = "aAAbbbb"
    Output: 3

ex2

    Input: jewels = "z", stones = "ZZ"
    Output: 0
## 설명
간단한 dict문제이다

- solution1
1. 빈 딕셔너리를 만든후
2. jewles를 for문으로 받아 새로운 문자가 있으면 추가해주고
3. 기존의 문자가 있으면 갯수를 더해준다
4. jewles를 저장해놓은 dic에 스톤이 있으면 answer에 더해준다
5. 그후 결과를 출력

- solution2

jewels.count() 와 map을 활용하여 stones 문자열에 포함된 jewels의 갯수를 반환\
sum()으로 총 개수를 반환

## 알아야할점
- 딕셔너리의 개념과 기본적인 for문까지 알면 쉽게 풀수있다
- count
```python
list = ['a','b','b','c','e']
list.count('b') 
>>>3
