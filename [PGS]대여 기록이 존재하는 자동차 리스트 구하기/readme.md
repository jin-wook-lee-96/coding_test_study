# [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/157341)

## 문제
CAR_RENTAL_COMPANY_CAR 테이블과 CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블에서 자동차 종류가 '세단'인 자동차들 중 10월에 대여를 시작한 기록이 있는 자동차 ID 리스트를 출력하는 SQL문을 작성해주세요. 자동차 ID 리스트는 중복이 없어야 하며, 자동차 ID를 기준으로 내림차순 정렬해주세요.

## 테이블
<img width="361" alt="스크린샷 2023-03-09 오후 1 57 58" src="https://user-images.githubusercontent.com/107802548/223924149-fc8df38e-44d0-4611-9441-cc9e4ab3c12f.png">
<img width="309" alt="스크린샷 2023-03-09 오후 1 58 07" src="https://user-images.githubusercontent.com/107802548/223924178-41549e1d-05af-4da0-bee0-13c7647f77bc.png">



## 설명

1. 두개의 테이블을 CAR_ID로 조인
2. WHERE 절에서 세단과 10월에 대여시작기록이 있는것들을 작성
3. ORDER BY 에서 DESC로 내림차순 정렬후
4. DISTINCT로 중복제거

## 출력결과
<img width="478" alt="스크린샷 2023-03-09 오후 1 58 28" src="https://user-images.githubusercontent.com/107802548/223924318-b82bc047-1ed3-4b78-9748-7798ad310b2f.png">


## 알아야할점
- 기본적인 조인문법
- WHERE절 안에서 정해진 조건 작성법
- 원하는데로 정렬 하는 방법
