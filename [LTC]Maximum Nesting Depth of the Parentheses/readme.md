# [문제링크](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/)

## 문제
문자열이 다음 중 하나를 충족하는 경우 유효한 괄호 문자열(VPS로 표시)입니다:

빈 문자열 ""이거나 "(" 또는 ")"와 같지 않은 단일 문자입니다,
AB(A와 B가 연결된 A)로 작성할 수 있으며, 여기서 A와 B는 VPS입니다.
(A)로 작성할 수 있으며, 여기서 A는 VPS입니다.
마찬가지로 모든 VPS S의 중첩 깊이 깊이(S)를 다음과 같이 정의할 수 있습니다:

- depth("") = 0
- depth(C) = 0, 여기서 C는 "(" 또는 ")"와 같지 않은 단일 문자가 포함된 문자열입니다.
- depth(A + B) = max(depth(A), depth(B)), 여기서 A와 B는 VPS입니다.
- depth("(" + A + ")") = 1 + depth(A), 여기서 A는 VPS입니다.
- 예를 들어 "", "(()()", "(()(()())"는 (중첩 깊이가 0, 1, 2인) VPS이고 ")("와 "(()"는 VPS가 아닙니다.

문자열 s로 표현된 VPS가 주어지면, s의 중첩 깊이를 반환합니다.
## 설명
정리중,,
## 알아야할점
정리중,,
