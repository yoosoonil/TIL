# 문제 코드
from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count = {fruit: 1}
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)

# 발생오류 : 한 라인만 출력됨.
# 발생원인 : fruit_count = [fruit: 1] 에서 초기화 방법의 오류.
# 해결방법 : fruit_count[fruit] = 1로 수정. 기존값이 없다면 초기값은 1.

# 수정 코드
from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        # fruit_count = [fruit: 1] 에서 fruit_count[fruit] = 1로 수정. 기존값이 없다면 초기값은 1.
        fruit_count[fruit] = 1  
    else:
        fruit_count[fruit] = fruit_count[fruit] + 1

pprint(fruit_count)