# [문제링크](https://leetcode.com/problems/split-with-minimum-sum/)

## 문제
양수 num이 주어졌을 때, 이를 음수가 아닌 두 개의 정수 num1과 num2로 나눕니다:

- num1과 num2의 연결은 num의 순열입니다.
- 즉, num1과 num2에서 각 자릿수의 발생 횟수의 합은 num에서 해당 자릿수의 발생 횟수와 동일합니다.
- num1과 num2는 선행 0을 포함할 수 있습니다.
- num1과 num2의 가능한 최소 합을 반환합니다.

Example 1

```
Input: num = 4325
Output: 59
Explanation: We can split 4325 so that
num1 is 24 and num2 is 35, giving a sum
of 59. We can prove that 59 is indeed
the minimal possible sum.
```
Example 1

```
Input: num = 687
Output: 75
Explanation: We can split 687 so that
num1 is 68 and num2 is 7, which would
give an optimal sum of 75.
```

## 설명
정렬을 이용한 문제풀이를 진행할 수 있다.
1. 리스트에 num값을 각각 넣어준다 
2. sort()를 이용하여 오름차순으로 정렬해준다
3. 최소가 되기위해 가장 홀수번쨰 작을수들로 조합
4. 그다음수는 짝수번째 작은수들로 조합
5. 두 수를 합하여 출력

## 알아야할점
- map함수를 이용해 int값을 list안에 숫자별로 넣을수 있어야함
- ```sort()``` 함수를 이용한 정렬
- ```''.join``` 을 이용하여 합치기
