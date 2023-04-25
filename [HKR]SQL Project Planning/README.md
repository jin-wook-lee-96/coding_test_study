# [문제링크](https://www.hackerrank.com/challenges/sql-projects/problem?isFullScreen=true)
## 문제
세 개의 열이 포함된 Projects 테이블이 제공됩니다: Task_ID, 시작 날짜, 종료 날짜. 테이블의 각 행에 대해 End_Date와 Start_Date의 차이가 1일이 되도록 보장합니다.

![1443819551-639948acc0-1](https://user-images.githubusercontent.com/107802548/234170872-2be360d8-3058-4266-814e-05c83fcac247.png)


작업의 End_Date가 연속적인 경우 동일한 프로젝트의 일부입니다. 사만다는 완료된 서로 다른 프로젝트의 총 개수를 찾고자 합니다.

프로젝트를 완료하는 데 걸린 일수별로 나열된 프로젝트의 시작 날짜와 종료 날짜를 오름차순으로 출력하는 쿼리를 작성합니다. 완료 일수가 같은 프로젝트가 두 개 이상 있는 경우 프로젝트의 시작 날짜 순으로 정렬합니다.

![1443819440-1c40e943a1-2](https://user-images.githubusercontent.com/107802548/234170960-040552ee-e059-4627-beca-5acf9fa4903e.png)

- sample output
```
2015-10-28 2015-10-29
2015-10-30 2015-10-31
2015-10-13 2015-10-15
2015-10-01 2015-10-04
```
