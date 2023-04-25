def solution(phone_book):
    dic = {}
    for phone_number in phone_book:
        dic[phone_number] = 1
    for phone_number in phone_book:
        prefix = ""
        for number in phone_number:
            prefix += number
            if prefix in dic and prefix != phone_number:
                return False
    return True

# 2. 접두어가 Hash map에 존재하는지 찾는다
# 3. 접두어를 찾아야 한다 (기존 번호와 같은 경우 제외)
