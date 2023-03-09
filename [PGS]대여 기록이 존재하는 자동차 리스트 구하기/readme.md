# [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/157341)

## 문제
CAR_RENTAL_COMPANY_CAR 테이블과 CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블에서 자동차 종류가 '세단'인 자동차들 중 10월에 대여를 시작한 기록이 있는 자동차 ID 리스트를 출력하는 SQL문을 작성해주세요. 자동차 ID 리스트는 중복이 없어야 하며, 자동차 ID를 기준으로 내림차순 정렬해주세요.

## 설명

1. 두개의 테이블을 CAR_ID로 조인
2. WHERE 절에서 세단과 10월에 대여시작기록이 있는것들을 작성
3. ORDER BY 에서 DESC로 내림차순 정렬후
4. DISTINCT로 중복제거

## 알아야할점
-기본적인 조인문법
-WHERE절 안에서 정해진 조건 작성법
-원하는데로 정렬 하는 방법
