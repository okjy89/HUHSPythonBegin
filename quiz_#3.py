#사이트 별로 비밀번호를 만들어 주는 프로그램을 작성하시오

#예) http://naver.com
# 규칙1 : http:// 부분은 제외 -> naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 -> naver
# 규칙3 : 남은 글자 중 처음 세자리(nav) + 글자 갯수(5) + 글자 내 'e' 갯수(1) + '!'로 구성

# 예) 생성된 비밀번호 : nav51!

site = 'http://naver.com'

rule_1 = site.replace('http://', '')

rule_2 = rule_1[:rule_1.index('.')]

password = rule_2[: 3] + str(len(rule_2)) + str(rule_2.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다.".format(site, password))